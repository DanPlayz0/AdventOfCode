def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents


def main():
  filecontents = readFile("input.txt")
  
  rounds = []

  for i in range(0, len(filecontents)):
    filecontents[i] = filecontents[i].strip()
    
    pairs = filecontents[i].split(",")
    pair1 = pairs[0].split("-")
    pair1[0] = int(pair1[0])
    pair1[1] = int(pair1[1])
    pair2 = pairs[1].split("-")
    pair2[0] = int(pair2[0])
    pair2[1] = int(pair2[1])

    if pair2[0] <= pair1[0] and pair1[0] <= pair2[1]:
      rounds.append(pairs)
    elif pair2[0] <= pair1[1] and pair1[1] <= pair2[1]:
      rounds.append(pairs)
    elif pair1[0] <= pair2[0] and pair2[0] <= pair1[1]:
      rounds.append(pairs)
    elif pair1[0] <= pair2[1] and pair2[1] <= pair1[1]:
      rounds.append(pairs)

  print(len(rounds))

if __name__ == '__main__':
  main()