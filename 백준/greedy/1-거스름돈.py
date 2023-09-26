n = int(input())
count = 0

while True:
  if n < 2:
    count = -1
    break
  
  if (n - 5) % 5 == 0 or (n - 5) % 2 == 0:
    n -= 5
  elif (n - 2) % 5 == 0 or (n - 2) % 2 == 0:
    n -= 2
  else:
    count = -1
    break

  count += 1  
  if n == 0:
    break

print(count)