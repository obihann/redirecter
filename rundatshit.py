#!/usr/bin/env python

import sys

from redirecter.redirecter import Redirecter

def main(argv):
    redirecter = Redirecter()

    try:
        uri = sys.argv[1]
    except(IndexError):
        print('A URL is required')
        sys.exit(2)

    site = redirecter.loadSite(uri)
    print(site)

if __name__ == "__main__":
    main = main(sys.argv[1:])
