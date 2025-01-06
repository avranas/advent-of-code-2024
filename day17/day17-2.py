import re

with open('day17-input.txt', 'r') as file:
    lines = [s for s in file.read().split("\n")]
    
reg = []
for i in range(3):
  reg.append(int(re.sub(r'[^0-9,]', '', lines[i])))

program = re.sub(r'[^0-9,]', '', lines[4]).split(",")

def combo(operand):
  if operand <= 3:
    return operand
  elif operand == 4:
    return regA
  elif operand == 5:
    return regB
  elif operand == 6:
    return regC
  elif operand == 7:
    print("this is reserved, whatever that means")
  else:
    print("something went wrong")  

def adv(operand):
  return int(regA / (2 ** combo(operand)))

programStr = ",".join(program)
i = 0
initRegA = 0

cache = {}

while True:
  # if initRegA % 10000 == 0:
  #   print(initRegA ,"/", reg[0])
  regA = initRegA
  regB = reg[1]
  regC = reg[2]
  output = ""
  newKeys = []
  while i < len(program):
    if (regA, regB, regC) in cache:
      if output != "":
        output += ","
      output += cache[(regA, regB, regC)]
      break
    newKeys.append((regA, regB, regC))
    opcode = program[i]
    operand = int(program[i+1])
    match opcode:
      case "0":
        regA = adv(operand)
      case "1":
        regB = regB ^ operand
      case "2":
        regB = combo(operand) % 8
      case "3":
        if regA == 0:
          break
        i = operand
        continue
      case "4":
        regB = regB ^ regC
      case "5":
        value = combo(operand) % 8
        if output != "":
          output += ","
        output += str(value)
      case "6":
        regB = adv(operand)
      case "7":
        regC = adv(operand)
    i += 2
  if output == programStr:
    print(output, programStr)
    print('breaking the future')
    break
  for key in newKeys:
    cache[key] = output
  initRegA += 1
  if initRegA % 100000 == 0:
    print(initRegA, 'ex: ', output, "   ||   ", programStr)


print('result: ', initRegA)