from collections import Counter

with open('day1-input.txt', 'r') as file:
    nums = [s for s in file.read().split() if s]

left = [int(num) for i, num in enumerate(nums) if i % 2 == 0]
right = [int(num) for i, num in enumerate(nums) if i % 2 == 1]
rightCounter = Counter(right)
total = 0

for num in left:
  total += rightCounter[num] * num
  
print(total)
