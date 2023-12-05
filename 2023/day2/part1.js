const { readFileSync } = require("fs");
const input = readFileSync("./input.txt", "utf-8").split("\n");

const max = { 'red': 12, 'green': 13, 'blue': 14 };
let valid = 0;

for (let line of input) {
  const [game, sets] = line.split(":").map((i) => i.trim());
  const gameid = Number(game.slice("Game ".length));

  let possible = true;
  for (let set of sets.split(';')) {
    let roundColors = {};
    for (let setColor of set.split(',')) {
      const [num, color] = setColor.trim().split(' ');
      if (roundColors[color] === undefined) roundColors[color] = 0;
      roundColors[color] += Number(num);
    }
    if (Object.entries(roundColors).some(([color, num]) => num > max[color])) possible = false; // Invalid
  }
  if (!possible) continue; 

  valid += gameid;
}

console.log(valid);