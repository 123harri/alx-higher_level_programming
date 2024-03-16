#!/usr/bin/node

/**
 * Function to return the number of occurrences of a specified element in a list.
 * @param {Array} list - The list to search for occurrences.
 * @param {*} searchElement - The element to count occurrences for.
 * @returns {number} - The number of occurrences of the searchElement in the list.
 */
exports.nbOccurences = function (list, searchElement) {
  return list.reduce(function (count, element) {
    return (element === searchElement) ? count + 1 : count;
  }, 0);
};
