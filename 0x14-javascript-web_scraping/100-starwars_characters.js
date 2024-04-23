#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from command-line argument
const id = process.argv[2];

// Construct the URL for the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Make a GET request to the specified URL
request.get(url, (err, response, body) => {
  // Check for error during the request
  if (err) {
    // Print the error
    console.log(err);
  } else {
    // Parse the response body
    const content = JSON.parse(body);
    // Get the list of characters
    const characters = content.characters;
    // Iterate over each character URL
    for (const characterUrl of characters) {
      // Make a GET request to fetch the character details
      request.get(characterUrl, (err, response, body) => {
        // Check for error during the request
        if (err) {
          // Print the error
          console.log(err);
        } else {
          // Parse the character details
          const characterData = JSON.parse(body);
          // Print the character name
          console.log(characterData.name);
        }
      });
    }
  }
});
