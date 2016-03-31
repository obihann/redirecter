import re
from urllib.parse import urlparse
from redirecter.utils.scraper import Scraper

class Page(object):
    def __init__(self, base):
        self.links = []
        self._page = urlparse(base)
        self._scraper = Scraper()

    def __str__(self):
        if not self.links: return ''

        self._clean()

        return '\n'.join(self.links)

    def _clean(self):
        temp = [] 

        for item in self.links:
            valid = True

            if item in temp: valid = False
            if item is self._page: valid = False
            if item is '/': valid = False

            if valid is True: temp.append(item)

        self.links = temp

    def append(self, value):
        url = urlparse(value)
        netloc = re.sub('(^w{3}.)', '', url.netloc)

        cleanPath = re.compile('(\/$)|(^\/)|(^(\.\.\/)+)', re.M)
        path = re.sub(cleanPath, '', url.path)

        if netloc is not self._page.netloc and netloc: return
        if not path or re.search('void', path):  return

        link = '%s://%s/%s' % (self._page.scheme, self._page.netloc, path)
        self.links.append(link)

        if len(self.links) % 2: self._clean()

    def scan(self):
        url = self._page.geturl()
        links = self._scraper.scrape(url)
        for link in links: self.append(link)
