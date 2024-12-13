with open('day12-input.txt', 'r') as file:
    grid = [list(s) for s in file.read().split("\n")]
    
ROWS = len(grid)
COLS = len(grid[0])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(node, y, x, visited):
  if y < 0 or x < 0 or y >= ROWS or x >= COLS:
    return [1, 0]
  if (y, x) in visited:
    return [0, 0]
  if grid[y][x] != node:
    return [1, 0]
  visited.add((y, x))
  res = [0, 0]
  for dy, dx in directions:
    perim, area = dfs(node, y + dy, x + dx, visited)
    res[0] += perim
    res[1] += area
  grid[y][x] = "."
  res[1] += 1
  return res

res = 0

for y in range(ROWS):
  for x in range(COLS):
    if grid[y][x] == ".":
      continue
    perim, area = dfs(grid[y][x], y, x, set())
    res += perim * area
    
print('result: ', res)
