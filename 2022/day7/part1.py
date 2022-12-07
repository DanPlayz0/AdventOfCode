def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents

directories = {"/~":0}
current = "/~"

def main():
  filecontents = readFile("input.txt")
  
  for index in range(0, len(filecontents)):
    line = filecontents[index].strip()
    if line[0] == "$":
      if line[2:4] == "cd":
        if line[5:6] == "/":
          current = "/~"
        elif line[5:] == "..":
          current = current[0:current.rfind("/")]
        else:
          current = current + "/" + (line[5:])
          directories.update({current:0})
      elif line[2:4] == "ls":
        pass
    elif line[0:3] == "dir":
      pass
    else:
      amount = int(line[:line.find(" ")])
      currentLocation = current
      for i in range(currentLocation.count("/")):
        directories[currentLocation] += amount
        currentLocation = currentLocation[:currentLocation.rfind("/")]

  output = 0
  for dir in directories:
    directorySize = directories[dir]
    if directorySize < 100000:
      output += directorySize
  print(output)

if __name__ == '__main__':
  main()