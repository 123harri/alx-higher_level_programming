#!/usr/bin/node

/**
 * Function to convert a number from base 10 to another base.
 * @param {number} base - The base to convert the number to.
 */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
