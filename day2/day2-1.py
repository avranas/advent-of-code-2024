with open('day2-input.txt', 'r') as file:
    levels = [s for s in file.read().split('\n')]
    
result = 0
for level in levels:
  nums = level.split(" ")
  safe = True
  state = "None"
  for i in range(1, len(nums)):
    prev = int(nums[i-1])
    num = int(nums[i])
    diff = abs(num - prev)
    if diff <= 0 or diff > 3:
      safe = False
      break
    if num < prev:
      if state == "Increasing":
        safe = False
        break
      state = "Decreasing"
    elif num > prev:
      if state == "Decreasing":
        safe = False
        break
      state = "Increasing"
  if safe:
    result += 1
    
print(result)
