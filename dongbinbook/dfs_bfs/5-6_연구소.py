from itertools import combinations
from collections import deque
import copy

# 값을 입력 받는다.
n, m = list(map(int, input().split()))
count = 0
result = 0 
queue = deque()
graph = []
blank = []
action_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for j in range(m):
  inputs = list(map(int, input().split()))
  graph.append(inputs)

for i in range(0, n):
  for j in range(0, m):
    if graph[i][j] == 0:
      blank.append((i, j))
    elif graph[i][j] == 2:
      queue.append((i, j))

print(blank)
def bfs(graph, queue):
  while len(queue) > 0:
    x, y = queue.popleft()
    graph[x][y] = 2
    for action in action_moves:
      dy, dx = action
      ny = y + dy
      nx = x + dx
      # 벗어나지 않았고 빈칸이라면
      if nx < m and ny < n and nx >= 0 and ny >= 0 and graph[ny][nx] == 0:
        queue.append((ny, nx))

comb = combinations(blank, 3)
print(list(comb))

for new_comb in list(comb):
  new_graph = copy.deepcopy(graph)
  new_queue = copy.deepcopy(queue)
  for i in new_comb:
    x, y = i
    new_graph[x][y] = 1
    # 남은 빈칸(0)을 전부 센다.
  bfs(new_graph, new_queue)
  for i in range(0, n):
    for j in range(0, m):
      if new_graph[i][j] == 0:
        count += 1
  result = max(result, count)
  count = 0

print(result)