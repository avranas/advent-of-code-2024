from collections import defaultdict

with open('day23-input.txt', 'r') as file:
    lines = [s.split("-") for s in file.read().split("\n")]

adj = defaultdict(list)

for a, b in lines:
  adj[a].append(b)
  adj[b].append(a)

def dfs(node, inNetwork):
  for next in adj[node]:
    inNetwork.add(next)
  for next in adj[node]:
    dfs(node)
  
for node in adj:
  dfs(node, set())