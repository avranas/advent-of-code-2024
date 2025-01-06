import re

with open('day17-input.txt', 'r') as file:
    lines = [s for s in file.read().split("\n")]
    
reg = []
for i in range(3):
  reg.append(int(re.sub(r'[^0-9,]', '', lines[i])))

regA = reg[0]
regB = reg[1]
regC = reg[2]
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

i = 0
output = ""

while i < len(program):
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
  
print('output:', output)
