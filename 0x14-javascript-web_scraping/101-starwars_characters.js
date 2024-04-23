#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from command-line argument
const movieId = process.argv[2];

// Construct the URL for the Star Wars API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make an HTTP GET request to the specified URL
request(apiUrl, (error, response, body) => {
  // Check for error during the request
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the JSON response body
  const movieData = JSON.parse(body);

  // Iterate through each character and print their name
  movieData.characters.forEach(characterUrl => {
    // Make a request to fetch data for the character
    request(characterUrl, (error, response, body) => {
      // Check for error during the request
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }
      // Parse the character data
      const characterData = JSON.parse(body);
      // Print the character name
      console.log(characterData.name);
    });
  });
});
