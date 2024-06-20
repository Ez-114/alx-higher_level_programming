#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let yIter = 0; yIter < this.height; yIter++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
