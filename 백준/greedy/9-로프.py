n = int(input())
numbers = []
dp = [0] * (n+1)

for _ in range(n):
  numbers.append(int(input()))

numbers.sort()

for i in range(n):
  dp[i] = (n-i) * numbers[i]

print(max(dp))