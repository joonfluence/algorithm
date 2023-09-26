position = list(input())
# a b c d e f g h
y, x = position
y = ord(y) - 96
x = int(x)

actions = ['LD', 'LU', 'RD', 'RU', 'UL', 'UR', 'DL', 'DR']
actions_move = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, -2), (1, -2), (2, -1), (2, 1)]
map = []
count = 0

for i in range(0, len(actions)):
  next_y, next_x = actions_move[i]
  if y + next_y < 1 or x + next_x < 1 or y + next_y > 8 or x + next_x > 8:
    continue
  count += 1

print(count)