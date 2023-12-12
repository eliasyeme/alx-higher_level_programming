#!/usr/bin/node
const MainSquare = require('./5-square');

class Square extends MainSquare {
  charPrint (c) {
    const char = c || 'X';
    console.log(`${char.repeat(this.width)}\n`.repeat(this.height).trimEnd());
  }
}

module.exports = Square;
