import sys

input_values = []
left_stack = list(sys.stdin.readline().rstrip())
right_stack = []

for _ in range(int(sys.stdin.readline())):
  value = list(sys.stdin.readline().split())
  if value[0] == 'L':
    if left_stack:
      right_stack.append(left_stack.pop())
  elif value[0] == 'D':
    if right_stack:
      left_stack.append(right_stack.pop())
  elif value[0] == 'P':
    left_stack.append(value[1])
  elif value[0] == 'B':
    if left_stack:
      left_stack.pop()

left_stack.extend(reversed(right_stack))
print(''.join(left_stack))