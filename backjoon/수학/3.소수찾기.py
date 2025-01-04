import math

n = int(input())
numbers = list(map(int, input().split()))
result = []
count = 0

def is_prime(numbers):
  global count
  for number in numbers:
    flag = 0
    if number == 1:
      continue
    if number == 2:
      count += 1
      continue

    for i in range(2, int(math.sqrt(number)) + 1):
      if number % i == 0:
        flag = 1
        break
    
    if flag == 0:
      count += 1
  return count

print(is_prime(numbers))