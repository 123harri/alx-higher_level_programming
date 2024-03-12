#!/usr/bin/node

/**
 * Function to return the number of occurrences of a specified element in a list.
 * @param {Array} list - The list to search for occurrences.
 * @param {*} searchElement - The element to count occurrences for.
 * @returns {number} - The number of occurrences of the searchElement in the list.
 */
exports.nbOccurrences = function (list, searchElement) {
  // Use the reduce method to count occurrences
  let nOccurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
