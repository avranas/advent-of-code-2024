with open('day4-input.txt', 'r') as file:
    grid = file.read().split('\n')
for i, row in enumerate(grid):
  grid[i] = list(row)

ROWS = len(grid)
COLS = len(grid[0])

result = 0
for y in range(1, ROWS - 1):
  for x in range(1, COLS - 1):
    if grid[y][x] == "A":
      pos = False
      neg = False
      if (grid[y+1][x+1] == "M" and grid[y-1][x-1] == "S") or (grid[y+1][x+1] == "S" and grid[y-1][x-1] == "M"):
        neg = True
      if (grid[y-1][x+1] == "M" and grid[y+1][x-1] == "S") or (grid[y-1][x+1] == "S" and grid[y+1][x-1] == "M"):
        pos = True
        if pos and neg:
          result += 1
          continue
        
print("result:", result)