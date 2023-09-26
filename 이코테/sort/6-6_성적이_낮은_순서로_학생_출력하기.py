n = int(input())
array = []
for _ in range(0, n):
  x, y = input().split()
  array.append((x, int(y)))

array.sort(key=lambda x: x[1])

for element in array:
  print(element[0], end=' ')