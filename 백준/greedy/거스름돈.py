# https://www.acmicpc.net/problem/14916

n = int(input())
coins = [5, 2]
count = 0

print(count)

while n != 0:
  print("minus")
  if n // coins[0] > 1:
    n = n - coins[0]
    count += 1
    print("hello")
  else:
    n = n - coins[1]
    count += 1
    print("hello2")

# 0이 될 때까지 
# # 해당 값이 5와 2로 구할 수 있는지 확인한다. 
# 5를 빼본다. 
# 2를 빼본다. 
