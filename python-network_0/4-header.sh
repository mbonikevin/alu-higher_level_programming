#!/bin/bash
# sending GET request with custom header
curl -sH "X-School-User-Id: 98" "$1"
