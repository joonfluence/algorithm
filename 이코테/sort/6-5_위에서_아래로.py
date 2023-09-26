n = int(input())
array = []

for _ in range(0, n):
  array.append(int(input()))

array.sort(reverse=True)
print(array)