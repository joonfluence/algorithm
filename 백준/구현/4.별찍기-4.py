n = int(input())

for number in range(n, 0, -1):
  spaces = " " * (n - number)
  stars = "*" * number
  print(spaces + stars)