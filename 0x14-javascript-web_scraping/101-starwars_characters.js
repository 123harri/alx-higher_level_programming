#!/usr/bin/node

const request = require('request');

// Function to fetch and print characters of a movie
function printMovieCharacters(movieId) {
    // Construct the URL for the Star Wars API endpoint to fetch movie details
    const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    // Make a GET request to fetch movie details
    request(movieUrl, (error, response, body) => {
        // Handle request errors
        if (error || response.statusCode !== 200) {
            console.error('Error fetching movie details:', error || `Status code: ${response.statusCode}`);
            return;
        }

        // Parse the JSON response
        const movieData = JSON.parse(body);

        // Iterate through the characters in the movie and print their names
        movieData.characters.forEach((characterUrl) => {
            // Make a GET request to fetch character details
            request(characterUrl, (charError, charResponse, charBody) => {
                // Handle request errors
                if (charError || charResponse.statusCode !== 200) {
                    console.error('Error fetching character details:', charError || `Status code: ${charResponse.statusCode}`);
                    return;
                }

                // Parse the JSON character data
                const characterData = JSON.parse(charBody);

                // Print the character's name
                console.log(characterData.name);
            });
        });
    });
}

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

// Print characters of the specified movie
printMovieCharacters(movieId);
