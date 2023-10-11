n, m = list(map(int, input().split()))

numbers = []
dp = [[0] * (m+1) for i in range(n+1)]

for _ in range(n):
  numbers.append(list(map(int, input().split())))

k = int(input())
input_values = []

for _ in range(k):
  input_values.append(list(map(int, input().split())))

for x in range(1, n+1):
    for y in range(1, m+1):
       dp[x][y] = dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1] + numbers[x-1][y-1]

for a, b, c, d in input_values:
    print(dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1])