#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the specified URL
request.get(apiUrl, (error, response, body) => {
  // If an error occurred during the request, print the error message
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const movieData = JSON.parse(body);

  // Print the title of the movie
  console.log(movieData.title);
});
