with open('day21-input.txt', 'r') as file:
    lines = [s for s in file.read().split("\n")]
    
print(lines)
numCoordX = {
  "7": 0,
  "8": 1,
  "9": 2,
  "4": 0,
  "5": 1,
  "6": 2,
  "1": 0,
  "2": 1,
  "3": 2,
  "0": 1,
  "A": 2,
}
numCoordY = {
  "7": 0,
  "8": 0,
  "9": 0,
  "4": 1,
  "5": 1,
  "6": 1,
  "1": 2,
  "2": 2,
  "3": 2,
  "0": 3,
  "A": 3,
}

priority = {
  "A": ["^", ">", "v", "<"],
  "^": ["v", "<", ">", "A"],
  "v": ["^", "<", ">", "A"],
  "<": ["v", "^", ">", "A"],
  ">": ["v", "^", "<", "A"]
}

keys1 = []

y = numCoordY["A"]
x = numCoordX["A"]

# def dfs(directions):
#   if len(directions) == 1

result = 0
for line in lines:
  for c in line:
    targetY = numCoordY[c]
    targetX = numCoordX[c]
    newKeys = []
    if x < targetX:
      newKeys.append(">")
    if y > targetY:
      newKeys.append("^")
    if x > targetX:
      newKeys.append("<")
    if y < targetY:
      newKeys.append("v")
      
    result += dfs(newKeys)
    
    print(newKeys)
    x = targetX
    y = targetY
print(keys1)

dirCoordX = {
  "^": 1,
  "A": 2,
  "<": 0,
  "v": 1,
  ">": 2,
}

dirCoordY = {
  "^": 0,
  "A": 0,
  "<": 1,
  "v": 1,
  ">": 1,
}

keys2 = []
y = dirCoordY["A"]
x = dirCoordX["A"]

for c in keys1:
  targetY = dirCoordY[c]
  targetX = dirCoordX[c]
  order = priority[c]
  for d in order:
    match d:
      case ">":
        while x < targetX:
          keys2.append(">")
          x += 1
      case "v":
        while y < targetY:
          keys2.append("v")
          y += 1
      case "^":
        while y > targetY:
          keys2.append("^")
          y -= 1
      case "<":
        while x > targetX:
          keys2.append("<")
          x -= 1
  keys2.append("A")

print(keys2)
keys3 = ""
for c in keys2:
  targetY = dirCoordY[c]
  targetX = dirCoordX[c]
  while x < targetX:
    keys3 += ">"
    x += 1
  while y < targetY:
    keys3 += "v"
    y += 1
  while y > targetY:
    keys3 += "^"
    y -= 1
  while x > targetX:
    keys3 += "<"
    x -= 1
  keys3 += "A"
print(keys3)
print(len(keys3))