with open('day6-input.txt', 'r') as file:
    grid = [list(s) for s in file.read().split("\n")]

ROWS = len(grid)
COLS = len(grid)


startY = 0
startX = 0
flag = False
for startY in range(ROWS):
  for startX in range(COLS):
    if grid[startY][startX] == "^":
      flag = True
      break
  if flag:
    break
  
result = 0

for obY in range(ROWS):
  print('progress: ', obY ,' / ', ROWS)
  for obX in range(COLS):
    if grid[obY][obX] == "#":
      continue
    prev = grid[obY][obX]
    grid[obY][obX] = "#"
    direction = "up"
    visited = set()
    y = startY
    x = startX
    while True:
      grid[y][x] = "X"
      if (direction, y, x) in visited:
        result += 1
        break
      visited.add((direction, y, x))

      match direction:
        case "up":
          if y == 0:
            break
          if grid[y-1][x] == "#":
            direction = "right"
          else:
            y -= 1
        case "down":
          if y == ROWS - 1:
            break
          if grid[y+1][x] == "#":
            direction = "left"
          else:
            y += 1
        case "left":
          if x == 0:
            break
          if grid[y][x-1] == "#":
            direction = "up"
          else:
            x -= 1
        case "right":
          if x == COLS - 1:
            break
          if grid[y][x+1] == "#":
            direction = "down"
          else:
            x += 1
    grid[obY][obX] = prev
    
print('result: ', result)
