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
      // If w or h is not a positive integer or equal to 0, create an empty object
      Object.create(null);
    }
  }

  /**
   * Method to print the rectangle using the character X.
   */
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  /**
   * Method to exchange the width and height of the rectangle.
   */
  rotate () {
    if (this.width && this.height) {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  /**
   * Method to double the width and height of the rectangle.
   */
  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
