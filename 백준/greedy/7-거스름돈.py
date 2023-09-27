money = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
  if money // coin > 0:
    count += money // coin
    money = money % coin

print(count)