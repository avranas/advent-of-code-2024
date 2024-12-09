
from collections import defaultdict

with open('day8-input.txt', 'r') as file:
    grid = [list(s) for s in file.read().split("\n")]
    
ROWS = len(grid)
COLS = len(grid)

cache = defaultdict(list)

for y in range(ROWS):
  for x in range(COLS):
    if grid[y][x] == ".":
      continue
    cache[grid[y][x]].append((y, x))

antinodes = set()

def inRange(y, x):
  return y >= 0 and x >= 0 and y < ROWS and x < COLS

for key, nodes in cache.items():
  if len(nodes) <= 1: continue
  for i in range(len(nodes)):
    a = nodes[i]
    for j in range(i + 1, len(nodes)):
      b = nodes[j]
      newAntinodeY = b[0]
      newAntinodeX = b[1]
      while inRange(newAntinodeY, newAntinodeX):
        antinodes.add((newAntinodeY, newAntinodeX))
        newAntinodeY += b[0] - a[0]      
        newAntinodeX += b[1] - a[1]
      newAntinodeY = a[0]
      newAntinodeX = a[1]
      while inRange(newAntinodeY, newAntinodeX):
        antinodes.add((newAntinodeY, newAntinodeX))
        newAntinodeY += a[0] - b[0]
        newAntinodeX += a[1] - b[1]
        
print('result: ', len(antinodes))
