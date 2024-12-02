with open('day2-input.txt', 'r') as file:
    levels = [s for s in file.read().split('\n')]

result = 0
for level in levels:
  nums = level.split(" ")
  for j in range(len(nums) + 1):
    safeFound = False
    levelCopy = nums.copy()[:j] + nums.copy()[j+1:]
    state = "None"
    unsafe = False
    for i in range(1, len(levelCopy)):
      prev = int(levelCopy[i-1])
      num = int(levelCopy[i])
      diff = abs(num - prev)
      if diff <= 0 or diff > 3:
        unsafe = True
        break
      if num < prev:
        if state == "Increasing":
          unsafe = True
          break
        state = "Decreasing"
      elif num > prev:
        if state == "Decreasing":
          unsafe = True
          break
        state = "Increasing"
    if not unsafe:
      result += 1
      safeFound = True
      break
  if safeFound:
    continue
    
print(result)
