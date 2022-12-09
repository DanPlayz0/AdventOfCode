def readFile(fileName):
  file = open(fileName)
  filecontents = file.readlines()
  file.close()
  return filecontents

input = readFile("input.txt")
forest = [[int(t) for t in row.strip()] for row in input]
height = len(forest)
width = len(forest[0])

high_scores = []
for x in range(width):
  col = [forest[i][x] for i in range(height)]

  for y in range(height):
    row = forest[y]
    this = row[x]

    dist_l = next((d for d in range(1, x) if row[x - d] >= this), x)
    dist_r = next((d for d in range(1, width - x) if row[x + d] >= this), width - x - 1)
    dist_u = next((d for d in range(1, y) if col[y - d] >= this), y)
    dist_d = next((d for d in range(1, height - y) if col[y + d] >= this), height - y - 1)

    high_scores.append(dist_l * dist_r * dist_u * dist_d)

print(max(high_scores))