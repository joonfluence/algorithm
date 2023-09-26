n, m = list(map(int, input().split()))
y, x, position = list(map(int, input().split()))
graph = []

d = [[0] * m for _ in range(n)]
d[y][x] = 1

for _ in range(n):
  graph.append(list(map(int, input().split())))

# 북, 동, 남, 서 
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def turn_left():
  global position
  position += 1
  if position > 3:
    position = 0

turn_time = 0
count = 0

while True:
  turn_left()
  nx = x + dx[position]
  ny = y + dy[position]

  # 육지이고 방문한 적 없고 맵 안이면
  if graph[ny][nx] == 0 and d[ny][nx] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1
  if turn_time == 4:
    nx = x - dx[position]
    ny = y - dy[position]
    if graph[ny][nx] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)
