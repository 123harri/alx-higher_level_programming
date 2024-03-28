#!/usr/bin/python3

"""
Takes GitHub credentials (username and personal access token)
as command-line argumenits and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_info = response.json()
        print("Your GitHub id is:", user_info['id'])
    else:
        print("Failed to fetch user info. Status code:", response.status_code)
