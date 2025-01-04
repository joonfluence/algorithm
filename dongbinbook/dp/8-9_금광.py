for _ in range(int(input())):
  n, m = list(map(int, input().split()))
  numbers = list(map(int, input().split()))
  dp = []

  for idx in range(0, len(numbers), m):
    dp.append(numbers[idx:idx+m])
  
  for j in range(1, m):
    for i in range(n):
      if i == 0:
        left_up = 0
      else:
        left_up = dp[i-1][j-1]
      if i == n-1:
        left_down = 0
      else:
        left_down = dp[i+1][j-1]

      left = dp[i][j-1]
      dp[i][j] = max(left_up, left, left_down) + dp[i][j]
  
  result = 0
  for i in range(n):
    result = max(result, dp[i][m-1])
  print(result)