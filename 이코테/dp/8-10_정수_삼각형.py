n = int(input())
dp = []

for _ in range(n):
  dp.append(list(map(int, input().split())))

print(dp)

# 0은 제외
for i in range(1, n):
  length = len(dp[i])
  for j in range(length):
    if j == 0:
      left_up = 0
    else:
      left_up = dp[i-1][j-1]
    if j == i: # up 값이 없는 경우 
      up = 0
    else:
      up = dp[i-1][j]
    dp[i][j] = dp[i][j] + max(up, left_up)

print(max(dp[n - 1]))