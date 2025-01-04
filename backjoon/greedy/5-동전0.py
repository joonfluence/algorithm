n, money = map(int, input().split())
coins = []
count = 0

for _ in range(n):
  coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
  if money // coin > 0:
    count += money // coin
    money = money % coin
  if money == 0:
    break

print(count)