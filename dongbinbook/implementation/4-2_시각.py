hour = int(input())
second = 60
minute = 60

count = 0

for i in range(0, hour+1):
  for j in range(0, minute):
    for k in range(0, second):
      time = str(i) + str(j) + str(k)
      if '3' in time:
        count += 1

print(count)