#!/usr/bin/node
const superSquare = require('./5-square');

class Square extends superSquare {
  charPrint (c) {
    const ch = c || 'X';
    for (let yIter = 0; yIter < this.width; yIter++) {
      console.log(ch.repeat(this.width));
    }
  }
}

module.exports = Square;
