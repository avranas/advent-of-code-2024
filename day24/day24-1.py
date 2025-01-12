from collections import defaultdict

with open('day24-input.txt', 'r') as file:
    sections = [s for s in file.read().split("\n\n")]

initValues = sections[0].split('\n')
lines = sections[1].split('\n')

adj = defaultdict(list)
ops = {}

cache = {}

for v in initValues:
  key = v[:3]
  value = v[5]
  cache[key] = int(value)
  

for line in lines:
  words = line.split(" ")
  gate1 = words[0]
  op = words[1]
  gate2 = words[2]
  nextGate = words[4]
  adj[nextGate].append(gate1)
  adj[nextGate].append(gate2)
  ops[nextGate] = op

def bt(node):
  gate1 = adj[node][0]
  if gate1 not in cache:
    bt(gate1)
  gate2 = adj[node][1]
  if gate2 not in cache:
    bt(gate2)
  op = ops[node]
  match op:
    case "XOR":
      cache[node] = cache[gate1] ^ cache[gate2]
    case "OR":
      cache[node] = cache[gate1] | cache[gate2]
    case "AND":
      cache[node] = cache[gate1] & cache[gate2]

for node in adj:
  bt(node)
  
zs = []
for key in cache:
  if key.startswith("z"):
    zs.append((key, cache[key]))
zs.sort(key=lambda v: v[0])

binaryString = ""
for i in range(len(zs)-1, -1, -1):
  z = zs[i]
  binaryString += str(z[1])


result = 0
for c in binaryString:
  result <<= 1
  if c == "1":
    result += 1
print('result', result)
  