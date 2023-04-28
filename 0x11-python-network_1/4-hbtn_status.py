#!/usr/bin/python3

"""
    Fetches the status of tehe url
    https://alx-intranet.hbtn.io/status usng requests module
"""

if __name__ == '__main__':
    import requests

    content = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(content.text)}')
    print(f'\t- content: {content.text}')
