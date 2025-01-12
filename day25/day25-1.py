with open('day25-input.txt', 'r') as file:
    sections = [s.split('\n') for s in file.read().split("\n\n")]
    
print(sections)

locks = []
keys = []

for section in sections:
  newThing = []
  for x in range(5):
    height = 0
    for y in range(1, 6):
      if section[y][x] == "#":
        height += 1
    newThing.append(height)
  if section[0] == "#####":
    locks.append(newThing)
  elif section[-1] == "#####":
    keys.append(newThing)
  else:
    print("Something went wrong")
    
print(locks)
print(keys)

result = 0

for lock in locks:
  for key in keys:
    fits = True
    for i in range(len(lock)):
      if lock[i] + key[i] > 5:
        fits = False
        break
    if fits:
      result += 1
      
print('result: ', result)