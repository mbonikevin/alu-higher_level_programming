#!/bin/bash
# 0-body_size.sh

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# sending a GET request to the URL and getting size of the response in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'