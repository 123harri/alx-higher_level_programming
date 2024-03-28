#!/bin/bash
# This script takes a URL as input, sends a request, and displays the size in bytes.
curl -s "${1}" | wc -c
