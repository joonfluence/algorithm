n = int(input())
numbers = list(map(int, input().split()))
result = []
count = 0

for number in numbers:
  flag = 0
  if number == 1:
    continue
  if number == 2:
    count += 1
    continue

  for i in range(2, number):
    if number % i == 0:
      flag = 1
      break
  
  if flag == 0:
    count += 1

print(count)