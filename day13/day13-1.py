import re
from collections import defaultdict

with open('day13-input.txt', 'r') as file:
    lines = [s for s in file.read().split("\n")]

aPress = []
bPress = []
prizeLocations = []

for i in range(0, len(lines), 4):
  ax, ay = re.sub(r'[^0-9,]', '', lines[i]).split(",")
  bx, by = re.sub(r'[^0-9,]', '', lines[i+1]).split(",")
  prizeX,  prizeY = re.sub(r'[^0-9,]', '', lines[i+2]).split(",")
  aPress.append((int(ax), int(ay)))
  bPress.append((int(bx), int(by)))
  prizeLocations.append((int(prizeX), int(prizeY)))
  
print(aPress)
print(bPress)
print(prizeLocations)

res = 0
for i in range(len(prizeLocations)):
  locationY, locationX = prizeLocations[i]
  cache = {}
  cache[(locationY, locationX)] = 0
  newCache = {}
  prevLen = 0
  pressesLeft = 100
  while pressesLeft > 0:
    newCache = {}
    for key in cache:
      y, x = key
      tokens = cache[key]
      
      aY, aX = aPress[i]
      newY = y - aY
      newX = x - aX
      if newY >= 0 and newX >= 0:
        newCache[(newY, newX)] =  cache[key] + 3
        if newY == 0 and newX == 0:
          break
      
      bY, bX = bPress[i]
      newY = y - bY
      newX = x - bX
      if newY < 0: continue
      if newX < 0: continue
      newCache[(newY, newX)] = cache[key] + 1
      if newY == 0 and newX == 0:
        break
    for key in newCache:
      cache[key] = newCache[key]
    if prevLen == len(cache):
      break
    prevLen = len(cache)
  pressesLeft -= 1
  print("progress: ", i, " / ", len(prizeLocations))
  if (0, 0) in cache:
    res += cache[(0, 0)]
print('result: ', res)    
    
    
  


