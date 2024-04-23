#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the URL to request from command-line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, (error, response) => {
  // If an error occurred during the request, print the error message
  if (error) {
    console.error(error);
    return;
  }
  // Print the status code of the response
  console.log(`code: ${response.statusCode}`);
});
