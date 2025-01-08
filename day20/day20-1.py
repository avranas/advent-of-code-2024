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
farDirections = [(0, 2), (2, 0), (-2, 0), (0, -2)]

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
    
timeHash[(endY, endX)] = time
result = 0

y = startY
x = startX
result = 0
time = 0
visited = set()
while not (y == endY and x == endX):
  visited.add((y, x))
  nextX = -1
  nextY = -1
  time += 1
  for i in range(len(directions)):
    dy, dx = directions[i]
    fy, fx = farDirections[i]
    if y+fy > 0 and y+fy < ROWS and x+fx > 0 and x+fx < COLS and grid[y+dy][x+dx] == "#" and grid[y+fy][x+fx] == "." and (y + fy, x + fx) not in visited:
      if timeHash[(y + fy, x + fx)] - time - 1 >= 100:
        result += 1
      # savedTime.append(timeHash[(y + fy, x + fx)] - time - 1)
    if grid[y+dy][x+dx] == "." and (y+dy, x+dx) not in visited:
      nextX = x + dx
      nextY = y + dy
  x = nextX
  y = nextY
  
print('result: ', result)
  