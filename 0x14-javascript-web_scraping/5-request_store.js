#!/usr/bin/node

// Import the 'request' module
const request = require('request');
// Import the 'fs' module
const fs = require('fs');

// Get the URL to request and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  // If an error occurred during the request, print the error message
  if (error) {
    console.error(error);
    return;
  }

  // Write the response body to the specified file path in UTF-8 encoding
  fs.writeFile(filePath, body, 'utf8', (err) => {
    // If an error occurred while writing to the file, print the error message
    if (err) {
      console.error(err);
      return;
    }
    console.log(`Webpage content successfully stored in ${filePath}`);
  });
});
