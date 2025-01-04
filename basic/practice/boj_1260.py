from collections import deque

# N : 정점의 개수
# M : 간선의 개수
# V : 탐색 시작하는 정점의 번호 
N, M, V = list(map(int, input().split()))
graph = [[] for i in range(n+1)]

for _ in range(m):
  start, dest = list(map(int, input().split()))
  graph[start].append(dest)
  graph[dest].append(start)

visited = [False] * 1001

def dfs(v):
  print(v, end=" ")
  visited[v] = True
  for i in sorted(graph[v]):
    if not visited[i]:
      dfs(i)

def bfs(v):
  queue = deque([v])
  visited[v] = True

  while queue:
    start = queue.popleft()
    print(start, end=' ')
    for i in sorted(graph[start]):
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(V)
print()
visited = [False] * 1001
bfs(V)