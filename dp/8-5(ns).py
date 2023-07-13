# 힌트 : 그리디 문제
n, m = map(int, input().split())
divider = 0
count = 0
coins = []
d = [0] * 10001

for _ in range(n):
  coin = input()
  coins.append(coin)

# 입력 값을 정렬한다.
coins.sort(reverse=True)

for i in range(len(coins)):
  # 값이 나눠진다면
  if m % coins[i] == 0:
    print("hello")
  
  # 가장 큰 수부터 나누기 시작한다. 
  divider = m // coins[i]
  count += divider
  print(count)

print(coins)