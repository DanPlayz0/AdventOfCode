def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents

def main():
  filecontents = readFile("input.txt")
  elfs = [0]
  elfIndex = 0
  for i in range(0, len(filecontents)):
    if filecontents[i] == "\n":
      elfIndex += 1
      elfs.append(0)
    else:
      elfs[elfIndex] += int(filecontents[i])
  
  print(sum(sorted(elfs)[-3:]))

if __name__ == '__main__':
  main()