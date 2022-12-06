def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents

def main():
  filecontents = readFile("input.txt")[0]
  for index in range(0, len(filecontents)-14):
    content = filecontents[index:index+14]
    if len(set(content)) == 14:
      print(index+14)
      break

if __name__ == '__main__':
  main()