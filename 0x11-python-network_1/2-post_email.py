#!/usr/bin/python3

"""
    This script takes url and email, and sends post req
    to the url with email as parameter
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    from urllib.parse import urlencode

    data = urlencode({"email": sys.argv[2]}).encode("ascii")
    with urllib.request.urlopen(sys.argv[1], data) as result:
        print(result.read().decode("utf-8"))
