a = input()
b = input()
n = len(a)
m = len(b)

dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, n+1):
  dp[i][0] = i
for j in range(1, m+1):
  dp[0][j] = j

for i in range(1, n+1):
  for j in range(1, m+1):
    if a[i-1] == b[j-1]:
      dp[i][j] = dp[i-1][j-1]
    else:
      # 교체 
      add = dp[i-1][j-1]
      # 삽입 
      delete = dp[i-1][j]
      # 삭제 
      replace = dp[i][j-1]
      dp[i][j] = min(add, delete, replace) + 1

print(dp[n][m])