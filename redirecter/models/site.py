class Site(dict):
    def __init__(self, outputLevel = 1):
        self._outputLevel = outputLevel

    def __str__(self):
        results = ''

        for key in self:
            results = "%s\n%s" % (results, key)

            if self._outputLevel is 1:
                for link in self[key].links:
                    results = "%s\n---> %s" % (results, link)

        return results
