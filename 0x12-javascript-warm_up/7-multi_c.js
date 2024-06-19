#!/usr/bin/node

const occurences = parseInt(process.argv[2]);
if (isNaN(occurences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occurences; i++) {
    console.log('C is fun');
  }
}
