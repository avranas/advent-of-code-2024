from collections import defaultdict

with open('day23-input.txt', 'r') as file:
    lines = [s.split("-") for s in file.read().split("\n")]

adj = defaultdict(list)

for a, b in lines:
  adj[a].append(b)
  adj[b].append(a)
  
triplets = set()

for key in adj:
  nextList = adj[key]
  for i in range(len(nextList) - 1):
    next1 = nextList[i]
    for j in range(i + 1, len(nextList)):
      next2 = nextList[j]
      if next2 in adj[next1]:
        newTriplet = [key, next1, next2]
        newTriplet.sort()
        if key.startswith('t') or next1.startswith('t') or next2.startswith('t'):
          triplets.add(tuple(newTriplet))
print('result: ', len(triplets))