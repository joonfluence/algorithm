# 4
# 1 3 1 5
n = int(input())
numbers = list(map(int, input().split()))
d = [0] * 100
d[0] = numbers[0]
d[1] = max(numbers[0], numbers[1])

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + numbers[i])

print(d[n-1])