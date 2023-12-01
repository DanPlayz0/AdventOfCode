const { readFileSync } = require("fs");
const input = readFileSync("./input.txt", "utf-8").split("\n");

let values = []
for(let i of input) {
  const num = i.replace(/[^0-9]/g,'');
  values.push(Number(num[0]+num[num.length-1]));
}
console.log(values.reduce((a,b) => a+b, 0));