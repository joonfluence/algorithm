# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
  # 금광 정보 입력 (n : 세로길이, m : 가로길이)
  n, m = map(int, input().split())
  array = list(map(int, input().split()))
    
  # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화 (n x m)
  dp = []
  idx = 0
  for i in range(n):
    dp.append(array[idx:idx + m])
    idx += m
  
  # j가 0인 경우, 왼쪽 값을 계산할 수 없으므로 제외 
  for j in range(1, m):
    for i in range(n):
      # 1) 왼쪽 위
      if i == 0:
        left_up = 0 # 예외처리 1) : 왼쪽 최상단인 경우, 고려하지 않음
      else:
        left_up = dp[i-1][j-1]
      # 2) 왼쪽 아래 
      if i == n - 1:
        left_down = 0 # 예외처리 2) : 왼쪽 최하단인 경우, 고려하지 않음
      else:
        left_down = dp[i+1][j-1] 
      # 3) 왼쪽
      left = dp[i][j-1] # 왼쪽의 경우에는 따로 예외처리 하지 않음
      dp[i][j] = dp[i][j] + max(left_up, left_down, left)
  
  result = 0
  # dp 테이블의 가장 오른쪽의 값 중 최댓값을 결과값으로 담는다 
  for i in range(n):
    result = max(result, dp[i][m-1])
  
  print(result)