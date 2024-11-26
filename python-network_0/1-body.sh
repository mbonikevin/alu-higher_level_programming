#!/bin/bash
# displaying body only for 200 status
curl -sL "$1" -w "%{http_code}" -o temp_response.txt | grep -q "200" && cat temp_response.txt