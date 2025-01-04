from collections import deque

# 주어진 입력을 받는다. 
n, m = list(map(int, input().split()))
graph = []
icecream = 0

for _ in range(n):
  graph.append(list(map(int, input())))

# 이동 경로를 지정한다
action_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0

def bfs(graph, position):
  global count
  queue = deque()
  queue.append(position)
  count += 1

  while queue:
    y, x = queue.popleft()
    # 물을 채운다 (방문처리)
    graph[y][x] = 1

    # 인접한 노드들을 방문한다
    for action in action_moves:
      dy, dx = action
      ny = y + dy
      nx = x + dx
      # 벗어나지 않았고 (방문하지 않았으면) 구멍이 뚫려 있다면 
      if nx < m and ny < n and nx >= 0 and ny >= 0 and graph[ny][nx] == 0:
        queue.append((ny, nx))

# 순서대로 점검한다
for i in range(0, n):
  for j in range(0, m):
    if graph[i][j] == 0:
      bfs(graph, (i, j))

print(count)