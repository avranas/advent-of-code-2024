from collections import deque

with open('day20-input.txt', 'r') as file:
    grid = [list(s) for s in file.read().split("\n")]
    
ROWS = len(grid)
COLS = len(grid[0])

startX = -1
startY = -1
endX = -1
endY = -1
picoseconds = 1
timeHash = {}
for currY, row in enumerate(grid):
  done = False
  for currX, box in enumerate(row):
    if box == "S":
      startX = currX
      startY = currY
    if box == "E":
      endX = currX
      endY = currY
      grid[currY][currX] = "."
    if box == ".":
      picoseconds += 1
      
times = []
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

x = startX
y = startY
result = 0
time = 0
visited = set()
while not (y == endY and x == endX):
  visited.add((y, x))
  timeHash[(y, x)] = time
  time += 1
  for dy, dx in directions:
    if (y+dy, x+dx) in visited:
      continue
    if grid[y+dy][x+dx] == ".":
      x = x + dx
      y = y + dy
      break
    
def bfs(startY, startX):
  movesLeft = 20
  queue = deque([(startY, startX)])
  newQueue = deque()
  visited = set([(startY, startX)])
  res = 0
  while queue and movesLeft >= 0:
    y, x = queue.popleft()
    if grid[y][x] == ".":
      if timeHash[(y, x)] - timeHash[(startY, startX)] - (20 - movesLeft) >= 100:
        res += 1
    for dy, dx in directions:
      newY, newX = dy + y, dx + x
      if (newY, newX) not in visited and newY >= 0 and newY < ROWS and newX >= 0 and newX < COLS:
        visited.add((newY, newX))
        newQueue.append((newY, newX))
    if not queue:
      queue = newQueue
      newQueue = deque()
      movesLeft -= 1
  return res
    
result = 0
timeHash[(endY, endX)] = time
y = startY
x = startX
result = 0
time = 0
visited = set()
while not (y == endY and x == endX):
  visited.add((y, x))
  nextX = 1
  nextY = 3
  grid[y][x] = "#"
  result += bfs(y, x)
  grid[y][x] = "."
  for i in range(len(directions)):
    dy, dx = directions[i]
    if grid[y+dy][x+dx] == "." and (y+dy, x+dx) not in visited:
      nextX = x + dx
      nextY = y + dy
  x = nextX
  y = nextY
  time += 1
  
print('result: ', result)
  