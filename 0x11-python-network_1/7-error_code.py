#!/usr/bin/python3

"""
    send req and print result, account for error codes
"""

if __name__ == "__main__":
    import sys
    import requests
    from requests.exceptions import HTTPError

    try:
        result = requests.get(sys.argv[1])
        result.raise_for_status()
    except HTTPError:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)
