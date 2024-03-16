#!/usr/bin/node

let numberOfPrintedArgs = 0;

/**
 * Function to print the number of arguments already printed and the new argument value.
 * @param {*} item - The argument value to print.
 */
exports.logMe = function (item) {
  console.log(`${numberOfPrintedArgs}: ${item}`);
  numberOfPrintedArgs++;
};
