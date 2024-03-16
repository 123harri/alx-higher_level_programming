#!/usr/bin/node

// Import the Square class
const ParentSquare = require('./5-square');

/**
 * Class representing a square.
 */
class Square extends ParentSquare {
  /**
   * Method to print the square using the specified character c.
   * If c is undefined, use the character X.
   * @param {string} [c] - The character to print the square with.
   */
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    // Print the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
