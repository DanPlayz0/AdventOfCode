const { readFileSync } = require("fs");
const input = readFileSync("./input.txt", "utf-8").split("\n");

const wordNums = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

let values = [];
for(let i of input) {
  let digits = i.split('');
  for (let index = 0; index < digits.length; index++) {
    const char = digits[index];
    const remainingSubstring = i.slice(index);
    for (const [word, value] of Object.entries(wordNums)) {
      if (remainingSubstring.startsWith(word)) {
        digits[index] = value;
        break;
      }
    }
    digits[index] = parseInt(digits[index]);
  }
  digits = digits.join('').replace(/[^0-9]/g,'');
  values.push(Number(digits[0]+digits[digits.length-1]));
}

console.log(values.reduce((a,b) => a+b, 0));