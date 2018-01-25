from bs4 import BeautifulSoup
import config


class HtmlParser():
    def __init__(self):
        self.base_url = config.BASE_URL

    def parser(self, url, response):
        if not response:
            return
        soup = BeautifulSoup(response, 'lxml')
        new_urls = self._get_new_url(soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_url(self, soup):
        try:
            urls = soup.find_all(attrs='UserLink-link')
            format_url = []
            for index, url in enumerate(urls):
                format_url.append(self.base_url + url.get('href') + '/followers')
            return format_url
        except:
            return None

    def _get_new_data(self, url, soup):
        data = {'url': url.split('?')[0]}
        name_span = soup.find('span', class_='ProfileHeader-name')
        if name_span:
            data['name'] = name_span.text
        else:
            data['name'] = url.split('/')[-2]
        headline = soup.find('span', class_='RichText ProfileHeader-headline')
        if headline:
            data['headline'] = headline.text
        return data
