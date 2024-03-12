#!/usr/bin/node

/**
 * Class representing a rectangle.
 */
class Rectangle {
  /**
   * Constructor for the Rectangle class.
   * @param {number} w - The width of the rectangle.
   * @param {number} h - The height of the rectangle.
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer, create an empty object
      Object.create(null);
    }
  }
}

module.exports = Rectangle;
