from redirecter.models.page import Page 
from redirecter.models.site import Site

class Redirecter(object):
    def __init__(self):
        self._outputLevel = 2
        self._site = Site(self._outputLevel)
    
    # create new site and page from link
    # scan page for links and add page to site
    # add links to site as pages
    def loadSite(self, home):
        self._home = home
        self._site[self._home] = Page(self._home)
        self._site[self._home].scan()
        self._addPages(self._site[self._home].links)

        return self._site

    # loop through all pages in the site
    # check if the page has links and if not scan the page
    # add links found in scan to site
    def _scanSite(self):
        for x in self._site:
            if not self._site[x].links:
                self._site[x].scan()
                self._addPages(self._site[x].links)

    # loop through all links
    # check if links are already pages
    # if new pages have been added trigger scan of site
    def _addPages(self, links, childPages = True):
        scan = False

        for link in links:
            page = Page(link)
            page.scan()

            if childPages:
                for x in page.links:
                    if x not in self._site: 
                        self._site[x] = Page(x)
                        scan = True

        if scan: self._scanSite()
