n = int(input())
input_values = []
stack = []
for _ in range(n):
  input_values.append(input().split())

for value in input_values:
  if value[0] == 'pop':
    if len(stack) > 0:
      print(stack.pop())
    else:
      print(-1)
  elif value[0] == 'push':
    stack.append(int(value[1]))
  elif value[0] == 'top':
    if len(stack) > 0:
      print(stack[-1])
    else:
      print(-1)
  elif value[0] == 'size':
    print(len(stack))
  elif value[0] == 'empty':
    if len(stack) > 0:
      print(0)
    else:
      print(1)