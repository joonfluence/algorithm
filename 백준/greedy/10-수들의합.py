n = int(input())
number_sum = 0
count = 0
i = 0

while number_sum <= n:
  i += 1
  number_sum += i
  if number_sum > n:
    break
  count += 1

print(count)