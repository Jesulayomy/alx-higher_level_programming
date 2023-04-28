#!/usr/bin/python3

""" Fetches the status of tehe url https://alx-intranet.hbtn.io/status """

if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as result:
        content = result.read()
        print('Body response:')
        print(f'\t- type: {type(content)}')
        print(f'\t- content: {content}')
        print(f"\t- utf8 content: {content.decode('utf-8')}")
