with open('day7-input.txt', 'r') as file:
    input = [s.split(" ") for s in file.read().split("\n")]

result = 0

def bt(nums, target, total, i=0, path=""):
  if i == len(nums):
    if total == target:
      return [path]
    return []
  return bt(nums, target, total + nums[i], i + 1, path + "+") + \
      bt(nums, target, total * nums[i], i + 1, path + "*") + \
      bt(nums, target, int(str(total) + str(nums[i])), i + 1, path + "|")

for line in input:
  target = int(line[0][:-1])
  nums = [int(num) for num in line[1:]]
  res = bt(nums[1:], target, nums[0])
  if len(res) > 0:
    result += target
  
print('result: ', result)
