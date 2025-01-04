import math
m, n = list(map(int, input().split()))
result = []

def is_prime(m, n):
  for number in range(m, n+1):
    flag = 0
    if number == 1:
      continue
    if number == 2:
      result.append(number)
      continue

    for i in range(2, int(math.sqrt(number)) + 1):
      if number % i == 0:
        flag = 1
        break
    
    if flag == 0:
      result.append(number)
  return result

for element in is_prime(m, n):
  print(element)