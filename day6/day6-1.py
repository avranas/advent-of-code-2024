with open('day6-input.txt', 'r') as file:
    grid = [list(s) for s in file.read().split("\n")]
print(grid)

ROWS = len(grid)
COLS = len(grid)
direction = "up"

print(grid)

y = 0
x = 0
flag = False
for y in range(ROWS):
  for x in range(COLS):
    if grid[y][x] == "^":
      flag = True
      break
  if flag:
    break

result = 1
while y > 0 and y < ROWS - 1 and x > 0 and x < COLS - 1:
  if grid[y][x] != "X":
    result += 1
  grid[y][x] = "X"
  if direction == "up" and grid[y-1][x] == "#":
    direction = "right"
  elif direction == "down" and grid[y+1][x] == "#":
    direction = "left"
  elif direction == "left" and grid[y][x-1] == "#":
    direction = "up"
  elif direction == "right" and grid[y][x+1] == "#":
    direction = "down"
  match direction:
    case "up":
      y -= 1
    case "down":
      y += 1
    case "left":
      x -= 1
    case "right":
      x += 1
print(grid)
print('result: ', result)
