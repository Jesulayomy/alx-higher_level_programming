#!/usr/bin/python3

""" post req to http://0.0.0.0:5000/search_user """

if __name__ == '__main__':
    import sys
    import requests

    q = ""

    try:
        q = sys.argv[1]
    except Exception:
        pass

    result = requests.post("http://0.0.0.0:5000/search_user", {"q": q})

    try:
        json_rep = result.json()
        if not json_rep:
            print("No result")
        else:
            print("[{}] {}".format(
                json_rep.get('id'),
                json_rep.get('name')))
    except Exception:
        print("Not a valid JSON")
