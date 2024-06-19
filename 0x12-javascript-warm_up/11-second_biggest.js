#!/usr/bin/node

const CLargs = process.argv;
let argv;

if (CLargs[2] === undefined) {
  console.log(0);
} else {
  argv = CLargs.slice(2);

  if (argv.length === 1) {
    console.log(0);
  } else if (argv.length > 1) {
    argv.sort((a, b) => { return a - b; });
    console.log(argv[argv.length - 2]);
  }
}
