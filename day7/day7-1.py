with open('day7-input.txt', 'r') as file:
    input = [s.split(" ") for s in file.read().split("\n")]

result = 0

def bt(nums, target, i=0, total=0):
  if i == len(nums):
    if total == target:
      return 1
    return 0
  return bt(nums, target, i + 1, total + nums[i]) + bt(nums, target, i + 1, total * nums[i])

for line in input:
  target = int(line[0][:-1])
  nums = [int(num) for num in line[1:]]
  if bt(nums, target) > 0:
    result += target
  
print('result: ', result)
