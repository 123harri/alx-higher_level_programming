#!/usr/bin/python3

"""
Sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""

if __name__ == '__main__':
    import sys
    from urllib import request, error

    args = sys.argv
    target_url = args[1]
    try:
        with request.urlopen(target_url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as http_err:
        print("Error code: {}".format(http_err.status))
