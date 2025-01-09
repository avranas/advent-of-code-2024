
with open('day22-input.txt', 'r') as file:
    lines = [s for s in file.read().split("\n")]

print(lines)

num = int(lines[0])

def mix(secret, given):
  return secret ^ given
  
def prune(secret):
  return secret % 16777216

result = 0
for line in lines:
  num = int(line)
  for i in range(2000):
    num2 = num * 64
    num3 = mix(num, num2)
    num4 = prune(num3)

    num5 = num4 // 32
    num6 = mix(num4, num5)
    num7 = prune(num6)

    num8 = num7 * 2048
    num9 = mix(num7, num8)
    num10 = prune(num9)
    num = num10
  # print('secret number: ', num)
  result += num
print('result: ', result)
  
