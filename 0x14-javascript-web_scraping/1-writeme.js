#!/usr/bin/node
// Script that writes a string to a file.
const fs = require('fs');
const file = process.argv[2];
const content = process.argv[3];

fs.writeFile(file, content, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
