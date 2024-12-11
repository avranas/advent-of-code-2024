with open('day11-input.txt', 'r') as file:
    input = [num for num in file.read().split(" ")]

cache = {}
def bt(stone, blinksLeft=75):
  if (stone, blinksLeft) in cache:
    return cache[(stone, blinksLeft)]
  if blinksLeft == 0:
    return 1
  res = []
  if stone == "0":
    res = bt("1", blinksLeft - 1)
  elif len(stone) % 2 == 0:
    half = len(stone) // 2
    left = stone[:half].lstrip('0')
    right = stone[half:].lstrip('0')
    res = bt(left if left else "0", blinksLeft - 1) + bt(right if right else "0", blinksLeft - 1)
  else:
    res = bt((str(int(stone) * 2024)), blinksLeft - 1)
  cache[(stone, blinksLeft)] = res
  return res

res = 0
for num in input:
  res += bt(num)
  
print('res', res)
