#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(`${'X'.repeat(this.width)}\n`.repeat(this.height).trimEnd());
  }
}

module.exports = Rectangle;
