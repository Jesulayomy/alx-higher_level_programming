#!/usr/bin/python3

"""
    Takes a url and returns the value of the
    X-Request-Id variable from its header
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as result:
        details = result.info()
        print(details.get('X-Request-Id'))
