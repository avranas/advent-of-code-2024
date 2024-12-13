with open('day12-input.txt', 'r') as file:
    grid1 = [list(s) for s in file.read().split("\n")]
with open('day12-input.txt', 'r') as file:
    grid2 = [list(s) for s in file.read().split("\n")]
    
ROWS = len(grid1)
COLS = len(grid1[0])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def areaDfs(node, y, x, visited):
  if y < 0 or x < 0 or y >= ROWS or x >= COLS:
    return 0
  if (y, x) in visited:
    return 0
  if grid1[y][x] != node:
    return 0
  visited.add((y, x))
  res = 0
  for dy, dx in directions:
    res += areaDfs(node, y + dy, x + dx, visited)
  grid1[y][x] = "."
  return res + 1

def perimDfs(node, y, x, visited, upSeen, downSeen, leftSeen, rightSeen):
  
  if grid2[y][x] != node:
    return 0
  if (y, x) in visited:
    return 0
  visited.add((y, x))
  
  res = 0
  
  # up
  if (y <= 0 or grid2[y][x] != grid2[y-1][x]) and (y, x) not in upSeen:
    upSeen.add((y, x))
    newY = y
    newX = x - 1
    # go left
    while newX >= 0 and grid2[newY][newX] == node and (newY, newX) not in upSeen and (y == 0 or grid2[newY-1][newX] != node):
      upSeen.add((newY, newX))
      newX -= 1
    newX = x + 1
    # go right
    while newX < COLS and grid2[newY][newX] == node and (newY, newX) not in upSeen and (y == 0 or grid2[newY-1][newX] != node):
      upSeen.add((newY, newX))
      newX += 1
    res += 1
    
  # down
  if (y >= ROWS - 1 or grid2[y][x] != grid2[y+1][x]) and (y, x) not in downSeen:
    downSeen.add((y, x))
    newY = y
    newX = x - 1
    # go left
    while newX >= 0 and grid2[newY][newX] == node and (newY, newX) not in downSeen and (y == ROWS - 1 or grid2[newY+1][newX] != node):
      downSeen.add((newY, newX))
      newX -= 1
    newX = x + 1
    # go right
    while newX < COLS and grid2[newY][newX] == node and (newY, newX) not in downSeen and (y == ROWS - 1 or grid2[newY+1][newX] != node):
      downSeen.add((newY, newX))
      newX += 1
    res += 1
  
  # left
  if (x <= 0 or grid2[y][x] != grid2[y][x-1]) and (y, x) not in leftSeen:
    leftSeen.add((y, x))
    newY = y - 1
    newX = x
    # go up
    while newY >= 0 and grid2[newY][newX] == node and (newY, newX) not in leftSeen and (x == 0 or grid2[newY][newX-1] != node):
      leftSeen.add((newY, newX))
      newY -= 1
    # go down
    newY = y + 1
    while newY < ROWS and grid2[newY][newX] == node and (newY, newX) not in leftSeen and (x == 0 or grid2[newY][newX-1] != node):
      leftSeen.add((newY, newX))
      newY += 1
    res += 1
    
  # right
  if (x >= COLS - 1 or grid2[y][x] != grid2[y][x+1]) and (y, x) not in rightSeen:
    rightSeen.add((y, x))
    newY = y - 1
    newX = x
    # go up
    while newY >= 0 and grid2[newY][newX] == node and (newY, newX) not in rightSeen and (x == COLS - 1 or grid2[newY][newX+1] != node):
      rightSeen.add((newY, newX))
      newY -= 1
    # go down
    newY = y + 1
    while newY < ROWS and grid2[newY][newX] == node and (newY, newX) not in rightSeen and (x == COLS - 1 or grid2[newY][newX+1] != node):
      rightSeen.add((newY, newX))
      newY += 1
    res += 1
    
  for dy, dx in directions:
    newY = y + dy
    newX = x + dx
    if newY < 0 or newX < 0 or newY >= ROWS or newX >= COLS:
      continue
    res += perimDfs(node, newY, newX, visited, upSeen, downSeen, leftSeen, rightSeen)
  return res

result = 0
for y in range(ROWS):
  for x in range(COLS):
    if grid1[y][x] == ".":
      continue
    area = areaDfs(grid1[y][x], y, x, set())
    perim = perimDfs(grid2[y][x], y, x, set(), set(), set(), set(), set())
    result += area * perim
    
print('result:', result)
