n = int(input())
steps = input().split()
actions = ['L', 'R', 'U', 'D']
actions_move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start = (1, 1)
x, y = start

for step in steps:
  next_step = ()
  
  if step == 'L':
    next_step = actions_move[0]
  elif step == 'R':
    next_step = actions_move[1]
  elif step == 'U':
    next_step = actions_move[2]
  elif step == 'D':
    next_step = actions_move[3]

  next_x, next_y = next_step
  if (y + next_y) <= 0 or (x + next_x) <= 0 or (y + next_y) > n or (x + next_x) > n:
    continue
  x += next_x
  y += next_y

print(y, x)