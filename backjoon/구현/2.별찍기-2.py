n = int(input())

for number in range(1, n+1):
  spaces = " " * (n - number)
  stars = "*" * number
  print(spaces + stars)