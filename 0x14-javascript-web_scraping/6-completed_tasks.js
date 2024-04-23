#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the API URL from command-line arguments
const apiUrl = process.argv[2];

// Make a GET request to the specified URL
request(apiUrl, function (error, response, body) {
  // If an error occurred during the request or the status code is not 200, print the error message
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
    return;
  }

  // Try parsing the JSON response body
  try {
    // Parse the JSON response body
    const todos = JSON.parse(body);

    // Initialize an object to store the count of completed tasks for each user ID
    const completed = {};

    // Iterate through each task
    todos.forEach((todo) => {
      // Check if the task is completed
      if (todo.completed) {
        // Increment the count of completed tasks for the user ID
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
    });

    // Format the output object with single quotes around the keys
    const output = `{${Object.entries(completed).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;

    // Print the output object
    console.log(Object.keys(completed).length > 2 ? output : completed);
  } catch (parseError) {
    // If an error occurred while parsing JSON, print the error message
    console.error('Error parsing JSON:', parseError);
  }
});
