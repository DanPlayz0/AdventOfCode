def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents


WIN = 6
DRAW = 3
LOSE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

endWithWin = 3
endWithDraw = 2
endWithLose = 1

letters = {
  "A": ROCK, "B": PAPER, "C": SCISSORS, 
  "X": ROCK, "Y": PAPER, "Z": SCISSORS
}

def main():
  filecontents = readFile("input.txt")
  
  rounds = []
  roundIndex = -1

  for i in range(0, len(filecontents)):
    col1, col2 = filecontents[i].strip().split(" ")
    col1, col2 = [letters[col1], letters[col2]]

    rounds.append(0)
    roundIndex += 1

    if col2 == endWithDraw:
      # print("Draw")
      rounds[roundIndex] = DRAW + col1
    elif col2 == endWithWin:
      # print("Win")
      rounds[roundIndex] = WIN
      if col1 == ROCK:
        rounds[roundIndex] += PAPER
      elif col1 == PAPER:
        rounds[roundIndex] += SCISSORS
      elif col1 == SCISSORS:
        rounds[roundIndex] += ROCK
    elif col2 == endWithLose:
      # print("Lose")
      rounds[roundIndex] = LOSE
      if col1 == ROCK:
        rounds[roundIndex] += SCISSORS
      elif col1 == PAPER:
        rounds[roundIndex] += ROCK
      elif col1 == SCISSORS:
        rounds[roundIndex] += PAPER
    # print(rounds[roundIndex])
  print(sum(rounds))

if __name__ == '__main__':
  main()