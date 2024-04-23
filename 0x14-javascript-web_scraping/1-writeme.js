#!/usr/bin/node

// Import the built-in Node.js 'fs' module.
const fs = require('fs');

// Get the file path and string to write from command-line arguments.
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the specified file in UTF-8 encoding.
fs.writeFile(filePath, content, 'utf8', (err) => {
  // If an error occurs during the writing process, print the error object to the console.
  if (err) {
    console.error(err);
    return;
  }
  console.log('File written successfully!');
});
