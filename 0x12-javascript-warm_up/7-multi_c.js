#!/usr/bin/node

const cis = 'C is fun';
const num = Number(process.argv[2]);

if (num) {
  for (let i = num; i > 0; i--) {
    console.log(cis);
  }
} else {
  console.log('Missing number of occurrences');
}
