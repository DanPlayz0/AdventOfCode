def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents

def main():
  filecontents = readFile("input.txt")[0]
  for index in range(0, len(filecontents)-4):
    content = filecontents[index:index+4]
    if len(set(content)) == 4:
      print(index+4)
      break

if __name__ == '__main__':
  main()