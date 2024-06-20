#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  function increment () {
    count++;
  }

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      increment();
    }
  }
  return count;
};
