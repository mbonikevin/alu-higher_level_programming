#!/usr/bin/python3
"""Sending a POST request to the givven URL"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    content = urllib.parse.urlencode({'email': email}).encode('utf-8')

    req = urllib.request.Request(url, data=content, method='POST')
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
