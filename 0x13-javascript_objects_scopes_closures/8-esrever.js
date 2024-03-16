#!/usr/bin/node

/**
 * Function to return the reversed version of a list.
 * @param {Array} list - The list to reverse.
 * @returns {Array} - The reversed version of the input list.
 */
exports.esrever = function (list) {
  const reversedList = [];

  // Iterate over the original list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
