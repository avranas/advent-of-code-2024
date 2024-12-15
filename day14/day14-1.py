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

for i in range(len(velocity)):
  seconds = 0
  while seconds < 100:
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
    seconds += 1

nw = 0
ne = 0
sw = 0
se = 0

for pY, pX in position:
  if pY < ROWS // 2:
    if pX < COLS // 2:
      nw += 1
    elif pX >= (COLS // 2) + 1:
      ne += 1
  elif pY >= (ROWS // 2) + 1:
    if pX < COLS // 2:
      sw += 1
    elif pY >= (COLS // 2) + 1:
      se += 1
      
print('result: ', nw * ne * sw * se)
