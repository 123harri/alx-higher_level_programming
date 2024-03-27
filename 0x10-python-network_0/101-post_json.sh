#!/bin/bash
# Sends a JSON POST request to the URL,with the contents of a file, and displays the body of the response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
