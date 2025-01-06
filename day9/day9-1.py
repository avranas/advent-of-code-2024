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

l = 0
r = len(blocks) - 1
while l <= r:
  while blocks[l] != ".":
    l += 1
  while blocks[r] == ".":
    r -= 1
  if l > r: break
  blocks[l], blocks[r] = blocks[r], blocks[l]
  
total = 0
for i, num in enumerate(blocks):
  if num == ".": break
  total += int(num) * i
  
print('total', total)
