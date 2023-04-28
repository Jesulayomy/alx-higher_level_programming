#!/usr/bin/python3

"""
    Lists 10 commits of a repo by a specific user from github
"""

if __name__ == '__main__':
    import requests
    import sys

    try:
        reponame = sys.argv[1]
        username = sys.argv[2]

        url = "https://api.github.com/repos/{}/{}/commits".format(
                username,
                reponame)
        result = requests.get(url)
        representation = result.json()
        for i in range(0, 10):
            print("{}: {}".format(
                representation[i].get('sha'),
                representation[i].get('commit').get('author').get('name')))
    except Exception:
        pass
