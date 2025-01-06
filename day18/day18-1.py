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

for x, y in lines:
  grid[int(y)][int(x)] = "#"
  
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

queue = deque([(0, 0)])
newQueue = deque()
visited = set()
moves = 0

while queue:
  y, x = queue.popleft()
  if y == maxY and x == maxX:
    print('moves: ', moves)
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
    grid[newY][newX] = "O"
  if not queue:
    queue = newQueue
    newQueue = deque()
    moves += 1
