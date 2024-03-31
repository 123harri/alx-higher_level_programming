#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token)
as command-line arguments and uses the GitHub API to display your id.
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    username = argv[1]
    password = argv[2]

    url = 'https://api.github.com/user'
    response = get(url, auth=(username, password))

    if response.status_code == 200:
        user_info = response.json()
        print(user_info.get('id'))
    else:
        print("None")
