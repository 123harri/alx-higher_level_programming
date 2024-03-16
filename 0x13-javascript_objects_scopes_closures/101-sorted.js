#!/usr/bin/node

// Importing the dictionary from 101-data.js
const dict = require('./101-data').dict;

// Function to invert the dictionary
function invertDictionary (originalDict) {
  const invertedDict = {};

  for (const userId in originalDict) {
    const occurrences = originalDict[userId];

    if (!(occurrences in invertedDict)) {
      invertedDict[occurrences] = [];
    }

    invertedDict[occurrences].push(userId);
  }

  return invertedDict;
}

// Computing the new dictionary
const invertedDict = invertDictionary(dict);

// Printing the new dictionary
console.log(invertedDict);
