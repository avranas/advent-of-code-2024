from collections import defaultdict


with open('day22-input.txt', 'r') as file:
    lines = [s for s in file.read().split("\n")]

num = int(lines[0])

def mix(secret, given):
  return secret ^ given
  
def prune(secret):
  return secret % 16777216

result = 0
allDiffs = []
allOrders = []
for line in lines:
  num = int(line)
  diffs = [-999]
  orders = [num % 10]
  for i in range(1999): # Might need to be 1999
    num2 = num * 64
    num3 = mix(num, num2)
    num4 = prune(num3)

    num5 = num4 // 32
    num6 = mix(num4, num5)
    num7 = prune(num6)

    num8 = num7 * 2048
    num9 = mix(num7, num8)
    num10 = prune(num9)
    diff =  -1 * ((num % 10) - (num10 % 10))
    diffs.append(diff)
    orders.append(num10 % 10)
    num = num10
  allDiffs.append(diffs)
  allOrders.append(orders)
bestResult = 0

allSequences = defaultdict(int)

for i in range(len(allDiffs)):
  diffs = allDiffs[i]
  orders = allOrders[i]
  sequences = defaultdict(int)
  for j in range(3, len(diffs)):
    sequence = (diffs[j-3], diffs[j-2], diffs[j-1], diffs[j])
    sequences[sequence] = max(sequences[sequence], orders[j])
  for key in sequences:
    allSequences[key] += sequences[key]
    
print('result', max(allSequences.values()))

# sortedSequences = sorted(allSequences.items(), key=lambda item: item[1])
# bestSequence = sortedSequences[-1][0]

# result = max(allSequences.values())
# for i in range(len(allDiffs)):
#   diffs = allDiffs[i]
#   orders = allOrders[i]
#   best = 0
#   for j in range(3, len(diffs)):
#     if bestSequence == (diffs[j-3], diffs[j-2], diffs[j-1], diffs[j]):
#       best = max(best, orders[j])
#   print(best)

# for count, sequence in enumerate(allSequences):
#   # print("progress: ", count, "/", len(allSequences))
#   a, b, c, d = sequence
#   sequenceTotal = 0
#   for i in range(len(allDiffs)):
#     diffs = allDiffs[i]
#     orders = allOrders[i]
#     maxBananas = 0
#     for j in range(3, len(diffs)):
#       if a == diffs[j-3] and b == diffs[j-2] and c == diffs[j-1] and d == diffs[j]:
#         maxBananas = max(maxBananas, orders[j])
#     sequenceTotal += maxBananas
#   if sequenceTotal > bestResult:
#     print(a, b, c, d, sequenceTotal)
#   bestResult = max(sequenceTotal, bestResult)
# print('result: ', bestResult)
