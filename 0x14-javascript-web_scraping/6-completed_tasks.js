#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the API URL from command-line arguments
const apiUrl = process.argv[2];

// Make a GET request using 'request' module to the specified URL
request(apiUrl, function (err, response, body) {
  // Check for successful response
  if (!err && response.statusCode === 200) {
    try {
      // Parse the JSON response body
      const todos = JSON.parse(body);

      // Object to store completed tasks per user
      const completedTasks = {};

      // Iterate through todos to count completed tasks per user
      todos.forEach((todo) => {
        if (todo.completed) {
          // Increment completed tasks count for the user
          if (completedTasks[todo.userId] === undefined) {
            completedTasks[todo.userId] = 1;
          } else {
            completedTasks[todo.userId]++;
          }
        }
      });

      // Convert completed tasks object to string format
      const output = `{${Object.entries(completedTasks).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;

      // Print the completed tasks per user
      console.log(Object.keys(completedTasks).length > 2 ? output : completedTasks);
    } catch (parseError) {
      // Handle JSON parsing error
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    // Handle request error
    console.error('Error:', err);
  }
});
