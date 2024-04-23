#!/usr/bin/node

// Import the built-in Node.js 'fs' module.
const fs = require('fs');

// Get the file path from the command-line arguments.
const filePath = process.argv[2];

// Read the content of the file specified by the file path.
// Use 'utf8' encoding to read the file as a UTF-8 encoded string.
fs.readFile(filePath, 'utf8', (err, data) => {
  // If an error occurs during the reading process, print the error object to the console.
  if (err) {
    console.error(err);
    return;
  }
  // Print the content of the file to the console.
  console.log(data);
});
