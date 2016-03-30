import re
from urllib.parse import urlparse

class Page(object):
    def __init__(self, base):
        
        reProtocol = re.compile('(^http[s]?)\:\/\/(.*)', re.M)
        urlGroups = re.search(reProtocol, base)

        self._keys = []
        self._page = urlparse(base)

    def __iter__(self):
        return iter(self._keys)

    def __getitem__(self, key):
        return self._keys[key]

    def __str__(self):
        self._clean()

        def prep(x): return self._page.scheme + '://' + self._page.path + '/' + x
        temp = [prep(x) for x in self._keys]

        return '\n'.join(temp)

    def _clean(self):
        temp = [] 

        for item in self._keys:
            valid = True

            if item in temp: valid = False
            if item is self._page: valid = False
            if item is '/': valid = False

            if valid is True: temp.append(item)

        self._keys = temp

    def append(self, value):
        url = urlparse(value)
        netloc = re.sub('(^w{3}.)', '', url.netloc)

        cleanPath = re.compile('(\/$)|(^\/)|(^(\.\.\/)+)', re.M)
        path = re.sub(cleanPath, '', url.path)

        if netloc is not self._page.netloc and netloc: return
        if not path or re.search('void', path):  return

        # match = re.compile('(\/$)|(^http[s]?:\/\/(w{3}.)*' + self._page.netloc + ')|(^\/)|(^(..\/)+)|(^\/){1}', re.M)
        # value = match.sub('', value)

        self._keys.append(path)

        if len(self._keys) % 2: self._clean()
