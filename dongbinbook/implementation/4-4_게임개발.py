n, m = list(map(int, input().split()))
x, y, direction = list(map(int, input().split()))

moves = ['U', 'R', 'D', 'L'] # 북 동 남 서
moves_action = [(-1, 0), (0, 1), (1, 0), (0, -1)]
graph = []
visited = [(x, y)]
turn_time = 0

for _ in range(n):
  graph.append(list(map(int, input().split())))

def turn_left():
  global direction, turn_time
  direction -= 1
  turn_time += 1

  if direction < 0:
    direction = 3
  return direction, turn_time

while True:
  nx, ny = 0, 0
  
  # 방향을 설정한다.
  direction, turn_time = turn_left()
  
  # 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면
  dx, dy = moves_action[direction]
  nx = x + dx
  ny = y + dy

  # 조건에 부합하면 이동한다.
  if nx <= n and nx > 0 and ny <= m and ny > 0 and graph[nx][ny] == 0 and (nx, ny) not in visited:
    x = nx
    y = ny
    visited.append((nx, ny))
    turn_time = -1
  
  # 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우
  if turn_time == 4:
    # 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다
    nx = x - dx
    ny = y - dy
    # 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우
    if graph[nx][ny] == 1:
      break
    else:
      x = nx
      y = ny
    turn_time = 0
  
print(len(visited))