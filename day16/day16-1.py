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

visited = {}
res = maxsize
queue = [(startY, startX, 'right', 0)]
while queue:
  y, x, direction, points = heapq.heappop(queue)
  if y == endY and x == endX:
    res = min(res, points)
    continue
  if (y, x) in visited and visited[(y, x)] < points:
    continue
  
  visited[(y, x)] = points
  for dy, dx, newDirection in directions:
    if grid[y+dy][x+dx] == ".":
      newPoints = points + 1 if direction == newDirection else points + 1001
      heapq.heappush(queue, (y + dy, x + dx, newDirection, newPoints))
      
print("result: ", res)
    
    
  
