with open('day15-input.txt', 'r') as file:
    data = [list(s) for s in file.read().split("\n")]
    
grid = []
moves = []

gridDone = False
for i in range(len(data)):
  if len(data[i]) == 0:
    gridDone = True
    continue
  if not gridDone:
    grid.append(data[i])
  else:
    moves += data[i]


y, x = -1, -1
done = False
for currY, row in enumerate(grid):
  if done: break
  for currX, box in enumerate(row):
    if box == "@":
      y = currY
      x = currX
      done = True
      break
    
print(y, x)
print(grid)
print(moves)

for move in moves:
  grid[y][x] = "@"
  # print("move: ", move, y, x)
  # for row in grid:
  #   print(row)
  # print("-------------")
  grid[y][x] = "."
  match move:
    case "<":
      if grid[y][x-1] == "#":
        continue
      offset = 1
      if grid[y][x-1] == ".":
        x -= 1
        continue
      while grid[y][x-offset] == "O":
        offset += 1
      if grid[y][x-offset] == "#":
        continue
      grid[y][x-offset] = "O"
      grid[y][x-1] = "."
      x -= 1
    case "v":
      if grid[y+1][x] == "#":
        continue
      offset = 1
      if grid[y+1][x] == ".":
        y += 1
        continue
      while grid[y+offset][x] == "O":
        offset += 1
      if grid[y+offset][x] == "#":
        continue
      grid[y+offset][x] = "O"
      grid[y+1][x] = "."
      y += 1
    case "^":
      if grid[y-1][x] == "#":
        continue
      offset = 1
      if grid[y-1][x] == ".":
        y -= 1
        continue
      while grid[y-offset][x] == "O":
        offset += 1
      if grid[y-offset][x] == "#":
        continue
      grid[y-offset][x] = "O"
      grid[y-1][x] = "."
      y -= 1
    case ">":
      if grid[y][x+1] == "#":
        continue
      offset = 1
      if grid[y][x+1] == ".":
        x += 1
        continue
      while grid[y][x+offset] == "O":
        offset += 1
      if grid[y][x+offset] == "#":
        continue
      grid[y][x+offset] = "O"
      grid[y][x+1] = "."
      x += 1
      
grid[y][x] = "@"      
print("move: ", move, y, x)
for row in grid:
  print(row)
print("-------------")

total = 0
for y in range(len(grid)):
  for x in range(len(grid[0])):
    if grid[y][x] == "O":
      total += (y * 100) + x
print('total:', total)
  