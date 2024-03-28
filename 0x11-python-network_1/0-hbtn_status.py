#!/usr/bin/python3

"""
This script fetches the status from https://alx-intranet.hbtn.io/status
and displays the body of the response.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')

    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
