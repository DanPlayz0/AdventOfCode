def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents

priority = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
  filecontents = readFile("input.txt")
  
  rounds = []

  for i in range(0, len(filecontents)):
    filecontents[i] = filecontents[i].strip()
    halfContLen = int(len(filecontents[i])/2)
    
    comp1 = filecontents[i][0:halfContLen]
    comp2 = filecontents[i][halfContLen:]

    intersected = set(comp1).intersection(set(comp2))
    rounds.append(list(intersected)[0])


  print(sum([priority.index(i) for i in rounds]))

if __name__ == '__main__':
  main()