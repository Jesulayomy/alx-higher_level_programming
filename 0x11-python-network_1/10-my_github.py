#!/usr/bin/python3

""" dispplays id """

if __name__ == "__main__":
    import sys
    import requests

    url = "https://api.github.com/user"
    params = {'Authorization': 'Bearer {}'.format(sys.argv[2])}

    result = requests.get(url, headers=params)
    try:
        print(result.json()["id"])
    except KeyError:
        print("None")
