with open('day4-input.txt', 'r') as file:
    grid = file.read().split('\n')
for i, row in enumerate(grid):
  grid[i] = list(row)

ROWS = len(grid)
COLS = len(grid[0])
expected = ['X', 'M', 'A', 'S']
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

def dfs(y, x, dy, dx, level=0):
  if y < 0 or x < 0 or y >= ROWS or x >= COLS:
    return False
  if grid[y][x] != expected[level]:
    return False
  if level == 3 and grid[y][x] == "S":
    return True
  prev = grid[y][x]
  grid[y][x] = "."
  newY = y + dy
  newX = x + dx
  if dfs(newY, newX, dy, dx, level + 1):
    grid[y][x] = prev
    return True
  grid[y][x] = prev
  return False
  
result = 0
for y in range(ROWS):
  for x in range(COLS):
    for dy, dx in directions:
      if dfs(y, x, dy, dx):
        result += 1
        continue
      
print('result: ', result)
