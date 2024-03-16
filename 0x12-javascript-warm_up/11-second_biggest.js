#!/usr/bin/node
function findSecondLargest (arr) {
  const uniqueNumbers = [...new Set(arr.map(Number))];
  const sortedNumbers = uniqueNumbers.sort((a, b) => b - a);

  if (sortedNumbers.length >= 2) {
    return sortedNumbers[1];
  } else {
    return 0;
  }
}

const argsAsNumbers = process.argv.slice(2).map(Number);
const result = findSecondLargest(argsAsNumbers);

console.log(result);
