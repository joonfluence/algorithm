n, m = list(map(int, input().split()))
numbers = []

for _ in range(n):
  numbers.append(int(input()))

print(numbers)

d = [10001] * (m+1)
d[0] = 0

for i in range(n):
  for j in range(numbers[i], m+1):
    if d[j - numbers[i]] != 10001:
      d[j] = min(d[j], d[j - numbers[i]] + 1)

if d[m] != 10001:
  print(d[m])
else:
  print(-1)