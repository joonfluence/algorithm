from collections import deque

# 주어진 입력을 받는다. 
n, m = list(map(int, input().split()))
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

# 동쪽이나 남쪽으로만 이동
action_moves = [(1, 0), (0, 1)]
print(graph)
count = 0

def bfs(graph, position, count):
  queue = deque()
  queue.append(position)

  while queue:
    y, x = queue.popleft()
    # 물을 채운다 (방문처리)
    count += 1
    graph[y][x] = count
    print(y, x, count)

    # 인접한 노드들을 방문한다
    for action in action_moves:
      dy, dx = action
      ny = y + dy
      nx = x + dx
      # 벗어나지 않았고 괴물이 없다면
      if nx < m and ny < n and nx >= 0 and ny >= 0 and graph[ny][nx] == 1:
        queue.append((ny, nx))

# 순서대로 점검한다
bfs(graph, (0, 0), 0)
print(graph[4][5])
