#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];
const completed = {};
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body);
    for (const result of results) {
      if (result.completed === true) {
        if (completed[result.userId] === undefined) {
          completed[result.userId] = 1;
        } else {
          completed[result.userId] += 1;
        }
      }
    }
    console.log(completed);
  }
});
