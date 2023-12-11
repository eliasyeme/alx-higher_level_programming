#!/usr/bin/node

const nums = process.argv.map((n) => Number(n)).slice(2);
console.log(nums.sort((a, b) => b - a)[1] || 0);
