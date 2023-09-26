from collections import deque

n, m, k, x = list(map(int, input().split()))
graph = [[] for _ in range(0, n+1)]
d = [0 for _ in range(0, n+1)]
queue = deque()
queue.append(x)
count = 0

for _ in range(0, m):
  idx, value = list(map(int, input().split()))
  graph[idx].append(value)

def bfs(graph, queue, d):
  while queue:
    popIdx = queue.popleft()
    for i in graph[popIdx]:
      if d[i] == 0: # 방문한 적 없으면 
        d[i] = d[popIdx] + 1 # 거리를 누적합한다 
        queue.append(i)

bfs(graph, queue, d)

if k in d:
  print(d.index(k))
else:
  print(-1)