n = int(input())
numbers = []
stack = []
operands = []
is_same = True
cur = 1

for _ in range(n):
  number = int(input())
  while cur <= number:
    stack.append(cur)
    operands.append("+")
    cur += 1
  if stack[-1] == number:
    stack.pop()
    operands.append("-")
  else:
    print("NO")
    is_same = False
    break

if is_same:
  for op in operands:
    print(op)
