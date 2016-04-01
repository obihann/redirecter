import threading
import time
from queue import Queue

from redirecter.models.page import Page 
from redirecter.models.site import Site

class Redirecter(object):
    def __init__(self):
        self._outputLevel = 2
        self._q = Queue()
        self._site = Site(self._outputLevel)

        for i in range(8):
            t = threading.Thread(target=self._worker)
            t.daemon = True
            t.start()
        

    def _worker(self):
        while True:
            item = self._q.get()

            item.scan()
            self._addPages(item.links)

            self._q.task_done()
    
    # create new site and page from link
    # scan page for links and add page to site
    # add links to site as pages
    def loadSite(self, home):
        self._home = home
        self._site[self._home] = Page(self._home)

        start = time.perf_counter()
        self._q.put(self._site[self._home])
        self._q.join()

        return self._site

    # loop through all pages in the site
    # check if the page has links and if not scan the page
    # add links found in scan to site
    def _scanSite(self):
        for x in self._site:
            if not self._site[x].links:
                self._q.put(self._site[x])

    def _scanPage(self, link, childPages = False):
        if link not in self._site:
            page = Page(link)
            page.scan()

            if childPages:
                for x in page.links:
                    if x not in self._site: 
                        self._site[x] = Page(x)
                        return True

        return False

    # loop through all links
    # check if links are already pages
    # if new pages have been added trigger scan of site
    def _addPages(self, links, childPages = True):
        scan = False

        for link in links:
            scan = self._scanPage(link, childPages)

        if scan: self._scanSite()
