n, m = map(int, input().split())
# 캐릭터의 현재 위치와 방향
x, y, direction = map(int, input().split())
d = []

# 방문정보 0으로 초기화, 방문하면 1 할당
for _ in range(n):
  d.append([0] * m)

print(d)
d[x][y] = 1

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 순서대로 : 좌 하 우 상
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1] 

def turn_left():
   global direction
   direction -= 1
   if direction == -1: # 북쪽을 보고 있으면
      direction = 3

print(array)
# 시뮬레이션 시작 
count = 1
turn_time = 0
while True:
   turn_left()
   nx = x + dx[direction] # 이동했을 때 x값
   ny = y + dy[direction] # 이동했을 때 y값
   if d[nx][ny] == 0 and array[nx][ny] == 0: # 가보지 않았고 육지이면
      d[nx][ny] = 1 # 방문처리
      print("before: ", x, y, end=" ")
      # 캐릭터 이동
      x = nx
      y = ny
      print("after: ",x, y, end=" ")
      count += 1
      turn_time = 0
      continue
   else:
      turn_time += 1
   # 네 방향 전부 갈 수 없는 경우
   if turn_time == 4:
    print("x y ", x, y)
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 이동한다 
    if array[nx][ny] == 0:
       x = nx
       y = ny
    # 바다인 경우 멈춘다
    else:
       break
    turn_time = 0

print(count)