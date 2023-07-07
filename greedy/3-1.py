import math

def greedy(money):
  coins = [500, 100, 50, 10]
  count = 0
  
  for coin in coins:
    if money == 0:
      break
    count += math.floor(money / coin)
    money = money % coin
  
  return count


countNum = greedy(5300)
print(countNum)