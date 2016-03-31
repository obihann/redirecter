import re
import sys
import urllib
from html.parser    import HTMLParser
from urllib.request import urlopen

class Scraper(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                 if key == 'href' and re.search('mailto\:', value) is None: 
                     self._links.append(value)

    def scrape(self, url):
        self._links = []
        try:
            response = urlopen(url)
        except(urllib.error.HTTPError):
            print('ERROR: Unable to index page %s' % url)
            return []

        ofType = re.search('text\/html', response.getheader('Content-Type'))

        if ofType != None:
            htmlBytes = response.read()
            htmlString = htmlBytes.decode('utf-8')
            self.feed(htmlString)
            
            return self._links
        else:
            return []
