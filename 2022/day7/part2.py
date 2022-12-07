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
  
  totalSpace = 70000000
  requiredSpace = 30000000
  deletionMinimum = directories["/~"] - (totalSpace - requiredSpace)

  posibilities = []
  for dir in directories:
    if deletionMinimum <= directories[dir]:
      posibilities.append(directories[dir])
  print(min(posibilities))

if __name__ == '__main__':
  main()