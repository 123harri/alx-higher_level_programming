#!/bin/bash
# Displays all HTTP methods accepted by the server for the given URL
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
