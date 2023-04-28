#!/usr/bin/python3

"""
    takes a url and sends a request to the it
    then displays the body of the response
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(sys.argv[1]) as result:
            print(result.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
