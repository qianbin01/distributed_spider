from data_storage_module import DataStorage
from extract_html_module import HtmlParser
from load_html_module import ZhiHuLoader
from url_manager_module import RedisUrlManager
import time
import multiprocessing


class MainScheduler:
    def __init__(self):
        self.parser_module = HtmlParser()
        self.url_manager_module = RedisUrlManager()

    def multi_process(self):
        load_module = ZhiHuLoader()
        while not self.url_manager_module.to_do_set_is_empty():
            url = self.url_manager_module.get_url_from_do_set()
            if url:
                page_url = str(url, encoding='utf-8') + '?page={page}'
                url = page_url.format(page=1)
                load_resp = load_module.load_html(url)
                parser_result = self.parser_module.parser(url, load_resp)
                if parser_result:
                    new_urls, new_data = parser_result
                    if new_urls:
                        for new_url in new_urls:
                            self.url_manager_module.put_url_to_do_set(new_url)
                    storage_module = DataStorage()
                    storage_module.save(new_data)
                    self.url_manager_module.put_url_to_over_set(url)
            time.sleep(0.5)

    def main(self):
        for i in range(10):
            p = multiprocessing.Process(target=self.multi_process)
            p.daemon = True
            p.start()
            time.sleep(1)
        while not self.url_manager_module.to_do_set_is_empty():
            time.sleep(5)
            pass
        print('Over HoHo')


if __name__ == "__main__":
    count = 0
    while count < 30:
        try:
            mainSpider = MainScheduler()
            mainSpider.main()
            count = count + 10
        except:
            count = count + 1
