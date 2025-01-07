with open('day19-input.txt', 'r') as file:
    lines = [s for s in file.read().split("\n")]
    
options = lines[0]
options = [o.strip() for o in options.split(",")]
patterns = lines[2:]

cache = {}

def bt(pattern, i=0):
  if (pattern, i) in cache:
    return cache[(pattern, i)]
  if i >= len(pattern):
    return 1
  res = 0
  for option in options:
    if pattern[i:].startswith(option):
      res += bt(pattern, i + len(option))
  cache[(pattern, i)] = res
  return res

total = 0
for i, pattern in enumerate(patterns):
  if bt(pattern) > 0:
    total += 1
    
print('result: ', total)
