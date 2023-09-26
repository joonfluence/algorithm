# 맵 크기 
n, m = map(int, input().split())
# 위치 정보 받기 
x, y, direction = map(int, input().split())
# 북 동 남 서 
action_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 캐릭터의 현재 위치를 방문 처리 
d[x][y] = 1
count = 1
# 턴 횟수 정보
turn_time = 0

# 맵 정보 초기화
game_map = []
for _ in range(0, n):
  game_map.append(list(map(int, input().split())))

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

while True:
  # 일단 왼쪽 방향부터 확인 
  turn_left()
  next_x, next_y = action_moves[direction]
  nx = x + next_x
  ny = y + next_y
  
  # 방문하지 않았고 그곳이 육지이면
  if d[nx][ny] == 0 and game_map[nx][ny] == 0:
    # 방문처리 
    d[nx][ny] = 1
    # 실제 이동 처리 
    x = nx
    y = ny 
    count += 1
    # 턴 초기화 
    turn_time = 0
    continue
  else:
    turn_time += 1
  if turn_time == 4:
    nx = x - next_x
    ny = x - next_y
    if game_map[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)

# 포인트
# 1. direction = 북, 동, 남, 서
# 2. 방문한 곳을 추적한다 = d[x][y]