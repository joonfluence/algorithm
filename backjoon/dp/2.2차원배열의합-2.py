# 숫자 입력 
n, m = list(map(int, input().split()))

numbers = []
dp = [[0] * (m+1) for i in range(n+1)]

for _ in range(n):
  numbers.append(list(map(int, input().split())))

# 테스트 케이스 입력
k = int(input())
cases = []

for _ in range(k):
  cases.append(list(map(int, input().split())))

for x in range(1, n+1):
    for y in range(1, m+1):
       dp[x][y]

for a, b, c, d in cases:
    print()