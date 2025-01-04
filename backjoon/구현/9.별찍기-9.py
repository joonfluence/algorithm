n = int(input())
count = 2*n-1
out_values = []

for number in range(count, 0, -2):
  spaces = " " * ((count - number) // 2)
  starts = "*" * number
  print(spaces + starts)

for number in range(3, count+2, 2):
  spaces = " " * ((count - number) // 2)
  starts = "*" * number
  print(spaces + starts)