#!/bin/bash
# Sends a request to the URL passed as an argument and displays only the status code of the response
curl -so /dev/null -w "%{http_code}" "$1"
