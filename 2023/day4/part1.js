const { readFileSync } = require("fs");
const input = readFileSync("./input.txt", "utf-8").split("\n");

let finalSum = 0;
for (let line of input) {
  const card = line.slice("Card XXX: ".length);
  const [winning, nums] = card.split(" | ").map((i) => i.trim());
  const winningNumbers = winning.split(" ");
  const numbers = nums.split(" ");
  const valid = numbers.filter((num) => winningNumbers.includes(num)).filter(Boolean);

  if (valid.length > 0) finalSum += Math.pow(2, valid.length - 1);
}

console.log(finalSum);