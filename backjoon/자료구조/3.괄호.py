n = int(input())
input_values = []
stack = []

for _ in range(n):
  input_values.append(input())

for line in input_values:
  stack = []
  counter = []
  duplicated = -1

  if len(line) % 2 == 1:
    print("NO")
    continue

  for j in line:
    stack.append(j)
  
  for j in range(len(line)):
    poped_value = stack.pop()
    if poped_value == ')':
      counter.append(poped_value)
    else:
      if len(counter) > 0:
        counter.pop()
      else:
        print("NO")
        duplicated = 1
        break
  
  if duplicated == -1:
    if len(stack) != 0 or len(counter) != 0:
      print("NO")
    else:
      print("YES")
