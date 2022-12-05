import re

def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents


def main():
  filecontents = readFile("input.txt")
  columns = []
  columnsEnd = 0

  for i in range(0, len(filecontents)):
    if filecontents[i] == "\n":
      columnsEnd = i-1
      for j in range(0, int(filecontents[columnsEnd].strip().split(" ")[-1:][0])):
        columns.append([])

  for i in range(0, columnsEnd):
    currentColumn = 0
    for j in range(0, len(filecontents[i]), 4):
      if filecontents[i][j:j+4].strip() == "":
        currentColumn += 1
      else:
        columns[currentColumn].append(filecontents[i][j:j+4].strip())
        currentColumn += 1
    
  for i in range(0, len(columns)):
    columns[i] = columns[i][::-1]
  
  for i in range(columnsEnd, len(filecontents)):
    matches = re.search("move ([0-9]+) from ([0-9]+) to ([0-9]+)", filecontents[i])
    if matches:
      steps = list(map(int, matches.groups()))
      for _ in range(steps[0]):
        columns[steps[2]-1].append(columns[steps[1]-1].pop())
  
  result = ""
  for i in range(0, len(columns)):
    result += columns[i][-1].replace("[", "").replace("]", "")
  print(result)

if __name__ == '__main__':
  main()