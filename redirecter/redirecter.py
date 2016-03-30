from redirecter.utils.scraper import Scraper
from redirecter.models.site    import Site

class Redirecter(object):
    def __init__(self):
        self.site = Site()
        self._scraper = Scraper()

    def scanSite(self, home):
        indexLinks = self._scraper.scrape(home)
        self.site[home] = indexLinks

        for page in indexLinks:
            uri = home + '/' + page
            links = self._scraper.scrape(uri)
            self.site[uri] = links

        return self.site
