#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the Star Wars API URL from command-line arguments
const apiUrl = process.argv[2];

// Character ID for "Wedge Antilles"
const characterId = '18';

// Make a GET request to the specified URL
request.get(apiUrl, (error, response, body) => {
  // If an error occurred during the request, print the error message
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const filmsData = JSON.parse(body);

  // Filter the films where "Wedge Antilles" is present
  const moviesWithCharacter = filmsData.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  // Print the number of movies where "Wedge Antilles" is present
  console.log(moviesWithCharacter.length);
});
