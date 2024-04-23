#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Function to fetch character data
const fetchCharacterData = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      const characterData = JSON.parse(body);
      resolve(characterData.name);
    });
  });
};

// Function to fetch movie data and print characters
const fetchAndPrintCharacters = async (movieId) => {
  try {
    // Construct the URL for the Star Wars API endpoint
    const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    // Make an HTTP GET request to the specified URL
    const movieResponse = await new Promise((resolve, reject) => {
      request(apiUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(JSON.parse(body));
      });
    });
    // Iterate through each character and print their name
    for (const characterUrl of movieResponse.characters) {
      const characterName = await fetchCharacterData(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

// Get the movie ID from command-line argument
const movieId = process.argv[2];

// Call the main function
fetchAndPrintCharacters(movieId);
