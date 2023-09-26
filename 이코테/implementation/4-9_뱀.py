# 1. 주어진 정보들(맵, 사과, 이동정보)을 입력 받는다. 
n = int(input())
k = int(input())
snake_map = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
actions_move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동, 남, 서, 북

# 1` 사과가 위치한 곳에 1을 표시한다.
for _ in range(k):
  a,b = map(int, input().split())
  snake_map[a][b] = 1

l = int(input())
move_directions = []

for _ in range(0, l):
  x, c = input().split()
  move_directions.append((int(x), c))

def change_direction(action_idx, key):
  if key == 'L':
    action_idx = (action_idx - 1) % 4
  else:
    action_idx = (action_idx + 1) % 4
  return action_idx

def simulate():
  cur_x, cur_y = 1, 1
  snake_map[cur_x][cur_y] = 2 # 1`` 자신이 있는 곳에 2를 표시한다. 
  action_idx = 0
  count = 1
  index = 0
  q = [(cur_x, cur_y)]

  while True:
    # 2. 뱀을 주어진 방향대로 이동시킨다.
    next_x, next_y = actions_move[action_idx]
    nx = cur_x + next_x
    ny = cur_y + next_y
    count += 1
    
    # 3. 이동하면서 맵에서 벗어나지는 않았는지, 자신의 몸에 부딪히진 않았는지 파악한다. 
    if nx < 1 or ny < 1 or nx > n or ny > n or snake_map[nx][ny] == 2:
      break
    else:
      cur_x, cur_y = nx, ny
      # 4. 사과를 먹지 않으면 이동 후에 꼬리를 제거한다 
      if snake_map[nx][ny] == 0:
        snake_map[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        snake_map[px][py] = 0
      # 5. 사과를 먹으면 몸의 길이가 늘어난다. 
      if snake_map[nx][ny] == 1:
        snake_map[nx][ny] = 2
        q.append((nx, ny))
    
    # 6. 시간이 일치하면 방향을 바꾼다
    if index < l and count == move_directions[index][0]:
      action_idx = change_direction(action_idx, move_directions[index][1])
      index += 1

  return count

print(simulate())