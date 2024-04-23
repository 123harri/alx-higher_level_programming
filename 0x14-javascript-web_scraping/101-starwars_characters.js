#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from command-line argument
const id = process.argv[2];

// Construct the URL for the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Make an HTTP GET request to the specified URL
request.get(url, (err, response, body) => {
  // Check for error during the request
  if (err) {
    // Print the error
    console.log(err);
  } else {
    // Parse the JSON response body
    const content = JSON.parse(body);
    // Get the list of characters
    const characters = content.characters;
    // Iterate over each character URL
    for (const character of characters) {
      // Make a request to fetch data for the character
      request.get(character, (err, response, body) => {
        // Check for error during the request
        if (err) {
          // Print the error
          console.log(err);
        } else {
          // Parse the character data
          const names = JSON.parse(body);
          // Print the character name
          console.log(names.name);
        }
      });
    }
  }
});
