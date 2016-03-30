import re
import sys
from html.parser    import HTMLParser
from urllib.request import urlopen

from redirecter.models.page import Page

class Scraper(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                 if key == 'href' and re.search('mailto\:', value) is None: 
                     self._page.append(value)

    def scrape(self, uri):
        self._page = Page(uri)
        response = urlopen(uri)
        ofType = re.search('text\/html', response.getheader('Content-Type'))

        if ofType != None:
            htmlBytes = response.read()
            htmlString = htmlBytes.decode('utf-8')
            self.feed(htmlString)
            
            return self._page
        else:
            return '', []
