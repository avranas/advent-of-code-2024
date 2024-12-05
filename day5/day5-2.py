from collections import defaultdict

with open('day5-input.txt', 'r') as file:
    input = file.read().split("\n\n")
    
edges = [e.split('|') for e in input[0].split("\n")]
rules = [e.split(',') for e in input[1].split("\n")]

adj = defaultdict(list)
for a, b in edges:
  adj[a].append(b)
  
def dfs(rule, path=[]):
  if len(rule) == 0:
    return path
  for i in range(len(rule)):
    next = rule[i]
    if len(path) > 0 and next not in adj[path[-1]]:
      continue
    res = dfs(rule[:i] + rule[i + 1:], path + [next])
    if res:
      return res
    
result = 0

for i, rule in enumerate(rules):
  print('progress: ', i, 'out of', len(rules))
  sortedRule = dfs(rule)
  # only add the incorrectly ordered
  i = 0
  while i < len(rule):
    if rule[i] != sortedRule[i]:
      result += int(sortedRule[len(sortedRule) // 2])
      break
    i += 1

print('result', result)
