#!/usr/bin/python3

""" post req to http://0.0.0.0:5000/search_user """

if __name__ == '__main__':
    import requests
    import sys

    try:
        q = sys.argv[1]
    except IndexError:
        q = ""

    result = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        json_rep = result.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if json_rep:
            print("[{}] {}".format(
                json_rep['id'],
                json_rep['name']))
        else:
            print("No result")
