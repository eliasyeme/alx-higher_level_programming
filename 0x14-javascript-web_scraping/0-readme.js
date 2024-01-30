#!/usr/bin/node
// script that reads and prints the content of a file.
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', function (err, data) {
  console.log(err || data);
});
