with open('day9-input.txt', 'r') as file:
    input = file.read()
    
blocks = []

id = 0
for i, num in enumerate(input):
  if i % 2 == 0:
    for j in range(int(num)):
      blocks.append(id)
    id += 1
  else:
    for j in range(int(num)):
      blocks.append(".")

print(blocks)
moved = set()

r = len(blocks) - 1
rightData = ""
while r >= 0:
  print('r', r)
  while blocks[r] == ".":
    r -= 1
  rightData = [blocks[r]]
  while blocks[r] == blocks[r-1]:
    rightData.append(blocks[r])
    r -= 1
  r -= 1
  l = 0
  leftData = []
  while l < r:
    while blocks[l] != ".":
      l += 1
    leftData = [blocks[l]]
    while l < len(blocks) - 1 and blocks[l] == blocks[l+1]:
      leftData.append(blocks[l])
      l += 1
    l += 1
    
    if len(leftData) >= len(rightData):
      if rightData[0] in moved:
        break
      moved.add(rightData[0])
      l2 = l - len(leftData)
      r2 = r + len(rightData)
      for _ in range(len(rightData)):
        blocks[l2], blocks[r2] = blocks[r2], blocks[l2]
        l2 += 1
        r2 -= 1
      break
      
total = 0
for i, num in enumerate(blocks):
  if num == ".": continue
  total += num * i
  
print('total', total)
