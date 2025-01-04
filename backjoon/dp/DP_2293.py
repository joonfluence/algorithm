"""
풀이과정

1. 주어진 입력을 받는다. n, k가 주어진다. 
2. 
"""

import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))
coins = [int(input()) for i in range(n)] # 코인의 종류를 적는다
dp = [0 for i in range(k+1)] # 사이즈 k+1만큼의 리스트를 선언한다 
dp[0] = 1 # 인덱스 0은 동전을 1개만 쓸 때의 경우의 수를 고려하기 위해 선언한다 

for i in coins:
  for j in range(i, k+1):
    if j-i >= 0:
      dp[j] += dp[j-i]

print(dp[k])