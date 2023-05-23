#!/usr/bin/node

const writeMe = require('fs');
const content = process.argv[3];

writeMe.writeFile(process.argv[2], 'utf-8', content, err => {
  if (err) {
    console.low(err);
  }
});
