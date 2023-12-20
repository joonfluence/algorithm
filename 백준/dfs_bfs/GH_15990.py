import sys
from collections import deque
input = sys.stdin.readline

# 위/아래/오른쪽/왼쪽/대각선
dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]

# 시작점이 주어지면 이동가능한 모든 점을 "방문했음" 상태로 만들기 -> 0
def BFS(x, y):
  queue = deque()
  queue.append([x,y])
  graph[y][x] = 0 # 방문 처리

  while queue:
    x, y = queue.popleft()
    for i in range(8):
      next_x = x + dx[i]
      next_y = y + dy[i]

      if 0 <= next_x < w and 0 <= next_y < h: # 범위 확인
        if graph[next_y][next_x] == 1: # 이동 가능 여부 확인
          queue.append([next_x, next_y])
          graph[next_y][next_x] = 0


# main
while(True):
  graph = list()
  w, h = map(int, input().split())

  # 0 0이 입력되면 종료된다.
  if (w == 0 and h == 0):
    break

  cnt = 0 # 섬 개수
  # input graph를 초기화 한다.
  for i in range(h):
    graph.append(list(map(int, input().split())))

  for i in range(h): # y
    for j in range(w): # x
      if graph[i][j] == 1:
        BFS(j, i)
        cnt += 1
  print(cnt)