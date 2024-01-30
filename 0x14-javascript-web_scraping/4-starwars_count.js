#!/usr/bin/node
// Script that prints the number of movies where the character
// “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];
let count = 0;
request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    for (const result of results) {
      for (const character of result.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
