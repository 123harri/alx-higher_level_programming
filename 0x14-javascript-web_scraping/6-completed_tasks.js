#!/usr/bin/node
// Import the 'request' module
const request = require('request');

// Make a GET request to the specified URL with JSON response
request.get(process.argv[2], { json: true }, (err, response, body) => {
  // Check for error during the request
  if (err) {
    // Print the error and exit
    console.log(err);
    return;
  }

  // Object to store completed tasks per user
  const completedTasks = {};

  // Iterate through each todo item in the response body
  body.forEach((todo) => {
    // Check if the task is completed
    if (todo.completed) {
      // Increment the count of completed tasks for the user
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 1;
      } else {
        completedTasks[todo.userId] += 1;
      }
    }
  });

  // Print the completed tasks per user
  console.log(completedTasks);
});
