n = int(input())
p = [0] + list(map(int, input().split()))
dp = [1e9 for _ in range(n+1)]
dp[0] = 0
dp[1] = p[1]

for i in range(2, n+1):
  for j in range(1, i+1):
    dp[i] = min(dp[i], dp[i-j] + p[j])

print(dp[n])