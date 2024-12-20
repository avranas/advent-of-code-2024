from collections import deque
import heapq
from sys import maxsize
with open('day16-input.txt', 'r') as file:
    grid = [list(s) for s in file.read().split("\n")]
    
def printGrid():
  print('--------------')
  for row in grid:
    s = ""
    for box in row:
        s += box
    print(s)

def printNewGrid(visited):
  for y, row in enumerate(grid):
    s = ""
    for x, box in enumerate(row):
      if (y, x) in visited:
        s += "O"
      else:
        s += grid[x][y]
    print(s)
  print('--------------')
    
startX = -1
startY = -1
endX = -1
endY = -1
for y, row in enumerate(grid):
  for x, box in enumerate(row):
    if box == "S":
      startX = x
      startY = y
      grid[y][x] = "."
    if box == "E":
      endY = y
      endX = x
      grid[y][x] = "."

directions = [(0, 1, "right"), (0, -1, "left"), (1, 0, "down"), (-1, 0, "up")]

bestScore = {}
res = maxsize
resVisited = set()

queue = [(startY, startX, 'right', 0, set())]
while queue:
  y, x, direction, points, visited = heapq.heappop(queue)
  if y == endY and x == endX:
    visited.add((y, x))
    if points < res:
      res = points
      resVisited = visited
    else:
      resVisited.update(visited, resVisited)
    continue
  if (y, x, direction) in bestScore and bestScore[(y, x, direction)] < points:
    continue
  bestScore[(y, x, direction)] = points
  newVisited = visited.copy()
  newVisited.add((y, x))
  for dy, dx, newDirection in directions:
    if grid[y+dy][x+dx] == ".":
      newPoints = points + 1 if direction == newDirection else points + 1001
      heapq.heappush(queue, (y + dy, x + dx, newDirection, newPoints, newVisited))
      
print("result: ", len(resVisited))
