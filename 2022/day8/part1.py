def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents

input = readFile("input.txt")
forest = [[int(t) for t in row.strip()] for row in input]

height = len(forest)
width = len(forest[0])
vis_count = 0

for x in range(width):
  col = [forest[i][x] for i in range(height)]
  for y in range(height):
    row = forest[y]
    this = forest[y][x]

    if all(t < this for t in row[:x]):
      vis_count += 1
    elif all(t < this for t in row[x + 1 :]):
      vis_count += 1
    elif all(t < this for t in col[:y]):
      vis_count += 1
    elif all(t < this for t in col[y + 1 :]):
      vis_count += 1
print(vis_count)