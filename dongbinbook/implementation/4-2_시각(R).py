hours = int(input()) + 1
minutes = 60
seconds = 60
count = 0

for i in range(0, hours):
  for j in range(0, minutes):
    for k in range(0, seconds):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)