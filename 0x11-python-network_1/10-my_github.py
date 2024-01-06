#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=(username, password))
    try:
        json = response.json()
        print(json.get('id'))
    except ValueError:
        print("Not a valid JSON")
