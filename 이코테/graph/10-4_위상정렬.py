from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n+1) # 진입차수
graph = [[] for i in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1 # 연결된 노드의 수만큼 진입차수를 증가시켜야 함

def topology_sort():
  result = []
  q = deque()

  for i in range(1, n+1):
    if indegree[i] == 0: # 초기 단계에서 진입차수가 0인 노드를 큐에 넣는다
      q.append(i)
  
  while q:
    now = q.popleft()
    result.append(now) # 출력값은 result에 담는다 
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0: # BFS 알고리즘에서의 방문 여부와 비슷함 (다만 여기선 조건이 변동된다)
        q.append(i)
  
  for i in result:
    print(i, end=' ')

topology_sort()