#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    const error = err;
    console.error(error);
  } else {
    const content = data;
    console.log(content);
  }
});
