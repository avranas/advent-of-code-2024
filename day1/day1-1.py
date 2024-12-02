import heapq

with open('day1-input.txt', 'r') as file:
    nums = [s for s in file.read().split() if s]

left, right = [], []
for i, num in enumerate(nums):
  heapq.heappush(left if i % 2 == 0 else right, int(num))
  
total = 0

while left or right:
  lNum = heapq.heappop(left)
  rNum = heapq.heappop(right)
  total += abs(lNum - rNum)

print(total)
