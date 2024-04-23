#!/usr/bin/node
// Import the 'request' module
const request = require('request');
// Import the 'fs' module
const fs = require('fs');

// Make a GET request using 'request' module to the specified URL
request.get(process.argv[2], (err, response, body) => {
  // Check for error during the request
  if (err) {
    // Print the error
    console.log(err);
  } else {
    // Write the response body to a file using 'fs' module
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      // Check for error during file write operation
      if (err) {
        // Print the error
        console.log(err);
      }
    });
  }
});
