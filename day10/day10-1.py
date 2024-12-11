from collections import defaultdict

with open('day10-input.txt', 'r') as file:
    grid = [list(s) for s in file.read().split("\n")]
    
ROWS = len(grid)
COLS = len(grid)

zeroes = set()

for y in range(ROWS):
  for x in range(COLS):
    if grid[y][x] == "0":
      zeroes.add((y, x))
      
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(y, x, visited):
  if (y, x) in visited:
    return 0
  visited.add((y, x))
  if grid[y][x] == "9":
    return 1

  res = 0
  for dy, dx in directions:
    newY = y + dy
    newX = x + dx
    if newY < 0 or newX < 0 or newY >= ROWS or newX >= COLS:
      continue
    if int(grid[y][x]) + 1 != int(grid[newY][newX]):
      continue
    res += dfs(newY, newX, visited)
  visited.remove((y, x))
  return res
    
result = 0

for y, x in zeroes:
  score = dfs(y, x, set())
  result += score
  
print('result', result)
