with open('day11-input.txt', 'r') as file:
    input = [num for num in file.read().split(" ")]

blinksLeft = 25

while blinksLeft > 0:
  print('blinksLeft', blinksLeft)
  newInput = []
  for num in input:
    if num == "0":
      newInput.append("1")
    elif len(num) % 2 == 0:
      half = len(num) // 2
      left = num[:half].lstrip('0')
      right = num[half:].lstrip('0')
      newInput.append(left if left else "0")
      newInput.append(right if right else "0")
    else:
      newInput.append(str(int(num) * 2024))
  input = newInput
  blinksLeft -= 1
  
print('result', len(newInput))
