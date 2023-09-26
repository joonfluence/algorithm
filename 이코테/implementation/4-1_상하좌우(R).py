n = int(input())
steps = input().split()
start = (1, 1)

actions = ['R', 'U', 'D', 'L']

# R U D L
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
y, x = start

for i in steps:
  ny, nx = y, x
  for j in range(4):
    if i == actions[j]:
      nx += dx[j]
      ny += dy[j]
  if nx < n and ny < n and nx > 0 and ny > 0:
    x = nx
    y = ny

print(y, x)