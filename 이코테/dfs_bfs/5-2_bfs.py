from collections import deque

# 1. 주어진 입력을 받는다.
n = int(input())
graph = [[]]

for i in range(1, n+1):
  graph.append(list(map(int, input().split())))

visited = [False for _ in range(n+1)]
queue = deque()

# 2. 초깃값 설정 및 방문 처리를 한다. 
queue.append(1)
visited[1] = True

def bfs(graph, queue, visited):
  while len(queue) > 0:
    idx = queue.popleft()
    print(idx)
    # 3. 인접한 노드부터 순회한다.
    for j in graph[idx]:
      if visited[j] is not True:
        visited[j] = True
        queue.append(j)

bfs(graph, queue, visited)