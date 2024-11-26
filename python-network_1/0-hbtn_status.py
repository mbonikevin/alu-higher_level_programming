#!/usr/bin/python3
"""
Fetches the status of the URL https://alu-intranet.hbtn.io/status
Displays the body response with:
- type of content
- raw content
- utf-8 decoded content
"""

import urllib.request

with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
