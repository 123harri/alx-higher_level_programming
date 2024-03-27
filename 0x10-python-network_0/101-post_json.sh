#!/bin/bash

# Sends a JSON POST request to the URL passed as the first argument,
# with the contents of a file passed as the second argument, and
# displays the body of the response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
