#!/usr/bin/python3

"""
    displays the value of X-Request-Id from the site passed in
"""

if __name__ == "__main__":
    import requests
    import sys

    try:
        result = requests.get(sys.argv[1])
        print(result.headers["X-Request-Id"])
    except Exception:
        pass
