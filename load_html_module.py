import requests
from utils import get_proxies


class ZhiHuLoader:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.proxies = get_proxies()

    def load_html(self, url):
        if self.proxies:
            r = requests.get(url, headers=self.headers, proxies=self.proxies)
            if r.status_code == 200:
                return r.text
            return None
        else:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                return r.text
            return None
