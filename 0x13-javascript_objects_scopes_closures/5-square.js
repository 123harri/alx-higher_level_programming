#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

/**
 * Class representing a square.
 */
class Square extends Rectangle {
  /**
   * Constructor for the Square class.
   * @param {number} size - The size of the square.
   */
  constructor (size) {
    // Call the constructor of the parent class (Rectangle) using super()
    super(size, size);
  }
}

module.exports = Square;
