class Site(object):
    def __init__(self, outputLevel = 1):
        self._outputLevel = outputLevel
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

            if self._outputLevel is 1:
                for link in self[key].links:
                    results = "%s\n---> %s" % (results, link)

        return results
