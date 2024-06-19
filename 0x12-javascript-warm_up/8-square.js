#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let yIter = 0; yIter < squareSize; yIter++) {
    console.log('X'.repeat(squareSize));
  }
}
