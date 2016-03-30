from redirecter.models.page import Page

class Site(object):
    def __init__(self):
        self._pages = dict()

    def __getitem__(self, key):
        return self._pages[key]

    def __setitem__(self, key, value):
        self._pages[key] = value

    def __iter__(self):
        return iter(self._pages)

    def __str__(self):
        results = ''

        for key in self:
            results = "%s\n%s" % (results, key)

            for link in self[key]:
                results = "%s\n---> %s/%s" % (results, key, link)

        return results

