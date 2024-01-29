# https://www.acmicpc.net/problem/2445

n = int(input())
count = 2*n-1
out_values = []

for number in range(2, count+2, 2):
  spaces = " " * ((count - number) // 2)
  starts = "*" * (number // 2)
  print(starts + spaces + starts)