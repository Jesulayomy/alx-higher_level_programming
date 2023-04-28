#!/usr/bin/python3

"""
    Sends apost request with the email and display response
"""

if __name__ == "__main__":
    import requests
    import sys

    result = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(result.text)
