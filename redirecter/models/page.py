import re
from urllib.parse import urlparse
from redirecter.utils.scraper import Scraper

class Page(object):
    def __init__(self, base):
        self.links = []
        self._page = urlparse(base)
        self._scraper = Scraper()

    def __str__(self):
        return '\n'.join(self.links)

    def _append(self, value):
        url = urlparse(value)
        netloc = re.sub('(^w{3}.)', '', url.netloc)

        cleanPath = re.compile('(\/$)|(^\/)|(^(\.\.\/)+)', re.M)
        path = re.sub(cleanPath, '', url.path)

        link = '%s://%s/%s' % (self._page.scheme, self._page.netloc, path)

        if netloc is not self._page.netloc and netloc: return
        if not path or re.search('void', path):  return
        if link in self.links: return
        if link is self._page.geturl(): return

        self.links.append(link)

    def scan(self):
        url = self._page.geturl()
        links = self._scraper.scrape(url)
        for link in links: self._append(link)
