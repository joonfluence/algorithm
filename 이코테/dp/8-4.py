d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for x in range(3, n+1):
  d[x] = d[x-1] + d[x-2]

print(d[6])