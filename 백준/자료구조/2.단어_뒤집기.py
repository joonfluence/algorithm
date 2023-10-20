n = int(input())
input_values = []
stack = []

for _ in range(n):
  input_values.append(input())

for inputs in input_values:
  for i in inputs.split():
    for j in i:
      stack.append(j)
    for j in i:
      print(stack.pop(), end="")
    stack.append(" ")
    print(stack.pop(), end="")
  print()
