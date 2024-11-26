#!/bin/bash
# sending GET request with custom header
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
