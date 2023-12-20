"""

풀이과정

1) 이동가능한 경우 : 상하좌우
2) dfs? bfs? bfs!
3) 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라 -> 해당 지점까지의 최단시간 구하기 -> 값을 계속 map에 갱신한다. 
4) 맵 꾸미기 : 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
5) 기존 bfs 문제랑 다른 점 : 시작 지점이 여러 곳일 수 있다. 

"""

from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
  for j in range(m):
    if matrix[i][j] == 1:
      queue.append([i, j])

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
        matrix[nx][ny] = matrix[x][y] + 1
        queue.append([nx, ny])

bfs()

for i in matrix:
  for j in i:
      if j == 0:
        print(-1)
        exit(0)
  res = max(res, max(i))
print(res - 1)