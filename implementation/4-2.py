n = int(input())
count = 0

for hour in range(n + 1):
  for minute in range(60):
    if '3' in str(hour):
      count = count + 3600
      break
    for second in range(60):
      if '3' in str(minute):
        count = count + 60
        break
      
      if '3' in str(second):
        count += 1
      

print(count)
