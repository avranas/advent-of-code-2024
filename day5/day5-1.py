from collections import defaultdict

with open('day5-input.txt', 'r') as file:
    input = file.read().split("\n\n")
    
edges = [e.split('|') for e in input[0].split("\n")]
rules = [e.split(',') for e in input[1].split("\n")]

adj = defaultdict(set)
for a, b in edges:
  adj[a].add(b)
  
result = 0

for rule in rules:
  for i in range(1, len(rule)):
    if i == len(rule) - 1:
      result += int(rule[len(rule) // 2])
      break
    prev = rule[i-1]
    curr = rule[i]
    next = rule[i+1]
    if prev in adj[curr]:
      break
    if next not in adj[curr]:
      break 
    
print('result: ', result)
