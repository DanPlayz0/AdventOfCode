def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents

priority = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
  filecontents = readFile("input.txt")
  
  rounds = []

  for id1,id2,id3 in [filecontents[a:a+3] for a in range(0,len(filecontents),3)]:
    sack1,sack2,sack3 = id1.strip(),id2.strip(),id3.strip()
    
    intersected = set(sack1).intersection(set(sack2)).intersection(set(sack3))
    
    rounds.append(list(intersected)[0])

  print(sum([priority.index(i) for i in rounds]))

if __name__ == '__main__':
  main()