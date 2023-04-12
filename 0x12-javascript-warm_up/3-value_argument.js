#!/usr/bin/env node

const argNoPath = process.argv.slice(2);
if (argNoPath[0] == null) {
  console.log('No argument');
} else {
  console.log(argNoPath[0]);
}
