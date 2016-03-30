from redirecter.utils.scraper import Scraper
from redirecter.models.site    import Site

site = Site()
scraper = Scraper()

def main(home):
    indexLinks = scraper.scrape(home)
    site[home] = indexLinks

    for page in indexLinks:
        uri = home + '/' + page
        links = scraper.scrape(uri)
        site[uri] = links

    return _site
