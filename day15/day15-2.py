from collections import deque

with open('day15-input.txt', 'r') as file:
    data = [list(s) for s in file.read().split("\n")]
    
gridData = []
moves = []

gridDone = False
for i in range(len(data)):
  if len(data[i]) == 0:
    gridDone = True
    continue
  if not gridDone:
    gridData.append(data[i])
  else:
    moves += data[i]

grid = []

for currY, row in enumerate(gridData):
  newRow = []
  for currX, box in enumerate(row):
    match box:
      case "#":
        newRow.append("#")
        newRow.append("#")
      case "O":
        newRow.append("[")
        newRow.append("]")
      case ".":
        newRow.append(".")
        newRow.append(".")
      case "@":
        y, x = currY, currX * 2
        newRow.append(".")
        newRow.append(".")
  grid.append(newRow)

def printGrid():
  print('--------------')
  for currY, row in enumerate(grid):
    s = ""
    for currX, box in enumerate(row):
      if currY == y and currX == x:
        s += "@"
      else:
        s += box
    print(s)

def push(y, x, yDiff):
  queue = deque([(y, x)])
  moveThese = []
  while queue:
    popY, popX = queue.popleft()
    moveThese.append((popY, popX))
    for i in range(2):
      newY = popY + yDiff
      newX = popX + i
      if grid[newY][newX] == "#":
        return False
      if grid[newY][newX] == "[":
        queue.append((newY, newX))
      elif grid[newY][newX] == "]":
        queue.append((newY, newX - 1))
  for y, x in moveThese:
    grid[y][x] = "."
    grid[y][x+1] = "."
  for y, x in moveThese:
    grid[y+yDiff][x] = "["
    grid[y+yDiff][x+1] = "]"
  return True
      
for move in moves:
  match move:
    case "<":
      if grid[y][x-1] == "#":
        continue
      offset = 1
      if grid[y][x-1] == ".":
        x -= 1
        continue
      while grid[y][x-offset] in ["[", "]"]:
        offset += 1
      if grid[y][x-offset] == "#":
        continue
      open = False
      for curr in range(x - 2, x - offset - 1, -1):
        grid[y][curr] = "[" if open else "]"
        open = not open
      grid[y][x-1] = "."
      x -= 1
    case ">":
      if grid[y][x+1] == "#":
        continue
      offset = 1
      if grid[y][x+1] == ".":
        x += 1
        continue
      while grid[y][x+offset] in ["[", "]"]:
        offset += 1
      if grid[y][x+offset] == "#":
        continue
      open = True
      for curr in range(x + 2, x + offset + 1 ):
        grid[y][curr] = "[" if open else "]"
        open = not open
      
      grid[y][x+1] = "."
      x += 1
    case "v":
      if grid[y+1][x] == "#":
        continue
      if grid[y+1][x] == ".":
        y += 1
        continue
      if grid[y+1][x] == "[":
        res = push(y + 1, x, 1)
      else:
        res = push(y + 1, x - 1, 1)
      if res:
        y += 1 
    case "^":
      if grid[y-1][x] == "#":
        continue
      if grid[y-1][x] == ".":
        y -= 1
        continue
      if grid[y-1][x] == "[":
        res = push(y - 1, x, -1)
      else:
        res = push(y - 1, x - 1, -1)
      if res:
        y -= 1

total = 0
for y in range(len(grid)):
  for x in range(len(grid[0])):
    if grid[y][x] == "[":
      total += (y * 100) + x
print('total:', total)
  