#!/usr/bin/node
const ls = require('./100-data').list;
const mappedLs = ls.map((x, idx) => x * idx);
console.log(ls);
console.log(mappedLs);
