import re

with open('day14-input.txt', 'r') as file:
    lines = [s for s in file.read().split("\n")]

position = []
velocity = []

for i in range(0, len(lines)):
  p, v  = re.sub(r'[^-?0-9, ]', '', lines[i]).split(" ")
  pX, pY = p.split(",")
  vX, vY = v.split(",")
  position.append([int(pY), int(pX)])
  velocity.append((int(vY), int(vX)))

COLS = 101
ROWS = 103

seconds = 0
seen = set()
while True:
  for i in range(len(velocity)):
    vY, vX = velocity[i]
    position[i][0] += vY
    position[i][1] += vX
    if position[i][0] < 0:
      position[i][0] += ROWS
    elif position[i][0] >= ROWS:
      position[i][0] -= ROWS
      
    if position[i][1] < 0:
      position[i][1] += COLS
    elif position[i][1] >= COLS:
      position[i][1] -= COLS
    
  grid = [["."] * COLS for _ in range(ROWS) ]
  for pY, pX in position:
    grid[pY][pX] = "X"
  for row in grid:
    print("".join(row))
  print("===============", seconds, " SECONDS", "===============================")  
  input("Press Enter to continue...")
    
  seconds += 1
  
#=============== 10403  SECONDS =============================== to see the same patterns again