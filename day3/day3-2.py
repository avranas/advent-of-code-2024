with open('day3-input.txt', 'r') as file:
    input = file.read()

def solution():
  validPrefix = {
    "m",
    "mu",
    "mul",
    "mul(",
    "d",
    "do",
    "do(",
    "do()",
    "don",
    "don'",
    "don't",
    "don't(",
    "don't()"
  }

  total = 0
  state = "prefix"
  prefix = ""
  num1 = ""
  num2 = ""
  on = True

  def reset():
    nonlocal state
    nonlocal prefix
    nonlocal num1
    nonlocal num2
    state = "prefix"
    prefix = ""
    num1 = ""
    num2 = ""

  for c in input:
    match state:
      case "prefix":
        prefix += c
        if prefix not in validPrefix:
          reset()
        if prefix == "mul(":
          state = "num1"
        elif prefix == "do()":
          on = True
          reset()
        elif prefix == "don't()":
          on = False
          reset()
      case "num1":
        if c.isnumeric():
          num1 += c
          if len(num1) > 3:
            reset()
        elif c == ",":
          if num1 == "":
            reset()
          else:
            state = "num2"
        else:
          reset()
      case "num2":
        if c.isnumeric():
          num2 += c
          if len(num2) > 3:
            reset()
        elif c == ")":
          if num2 == "":
            reset()
          else:
            # valid entry found
            if on:
              total += int(num1) * int(num2)
            reset()
        else:
          reset()
  return total

print(solution())