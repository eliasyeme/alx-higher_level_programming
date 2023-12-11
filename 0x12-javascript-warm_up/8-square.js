#!/usr/bin/node

const num = Number(process.argv[2]);

if (num) {
  for (let i = num; i > 0; i--) {
    console.log('x'.repeat(num));
  }
} else {
  console.log('Missing size');
}
