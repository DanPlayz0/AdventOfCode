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


letters = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

def main():
  filecontents = readFile("input.txt")
  
  rounds = []
  roundIndex = -1

  for i in range(0, len(filecontents)):
    col1, col2 = filecontents[i].strip().split(" ")
    col1, col2 = [letters[col1], letters[col2]]

    rounds.append(0)
    roundIndex += 1

    if col1 == col2:
      # print("Draw")
      rounds[roundIndex] = DRAW
      if col1 == ROCK:
        rounds[roundIndex] += ROCK
      elif col1 == PAPER:
        rounds[roundIndex] += PAPER
      elif col1 == SCISSORS:
        rounds[roundIndex] += SCISSORS
    else:
      if col1 == ROCK and col2 == SCISSORS:
        # print("You lose: Rock beats Scissors")
        rounds[roundIndex] = LOSE + SCISSORS
      elif col1 == ROCK and col2 == PAPER:
        # print("You win: paper covers rock")
        rounds[roundIndex] = WIN + PAPER
      elif col1 == PAPER and col2 == ROCK:
        # print("You lose: paper covers rock")
        rounds[roundIndex] = LOSE + ROCK
      elif col1 == PAPER and col2 == SCISSORS:
        # print("You win: scissors cut paper")
        rounds[roundIndex] = WIN + SCISSORS
      elif col1 == SCISSORS and col2 == PAPER:
        # print("You lose: scissors cut paper")
        rounds[roundIndex] = LOSE + PAPER
      elif col1 == SCISSORS and col2 == ROCK:
        # print("You win: rock breaks scissors")
        rounds[roundIndex] = WIN + ROCK
  print(sum(rounds))

if __name__ == '__main__':
  main()