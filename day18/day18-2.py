from collections import deque

with open('day18-input.txt', 'r') as file:
    lines = [s.split(",") for s in file.read().split("\n")]
    
maxX = 0
maxY = 0

for line in lines:
  maxX = max(maxX, int(line[0]))
  maxY = max(maxY, int(line[0]))

grid = []
for y in range(maxY + 1):
  newRow = []
  for x in range(maxX + 1):
    newRow.append(".")
  grid.append(newRow)

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
exitNotFound = False

for obXStr, obYStr in lines:
  obY = int(obYStr)
  obX = int(obXStr)
  grid[obY][obX] = "#"    
  if exitNotFound:
    break
  queue = deque([(0, 0)])
  newQueue = deque()
  visited = set()
  moves = 0
  while queue:
    y, x = queue.popleft()
    if y == maxY and x == maxX:
      break
    for dy, dx in directions:
      newY = y + dy
      newX = x + dx
      if newY < 0 or newY > maxY or newX < 0 or newX > maxX:
        continue
      if (newY, newX) in visited:
        continue
      visited.add((newY, newX))
      if grid[newY][newX] == "#":
        continue
      newQueue.append((newY, newX))
    if not queue:
      if not newQueue:
        print('No exit found! ', obX, obY)
        exitNotFound = True
        break
      queue = newQueue
      newQueue = deque()
      moves += 1
