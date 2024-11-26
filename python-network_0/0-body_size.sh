#!/bin/bash
# getting response size in byte
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'