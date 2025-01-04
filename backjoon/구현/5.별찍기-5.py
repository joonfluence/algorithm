n = int(input())
count = 2*n-1
out_values = []

for number in range(1, count+1, 2):
  spaces = " " * ((count - number) // 2)
  starts = "*" * number
  print(spaces + starts)