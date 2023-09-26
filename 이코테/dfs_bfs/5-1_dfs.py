# 주어진 입력을 받는다. 
n = int(input())
graph = [[]]

for i in range(1, n+1):
  graph.append(list(map(int, input().split())))

visited = [False for _ in range(n+1)]

# 초깃값 설정 및 방문 처리를 한다.
stack = []
stack.append(1)
visited[1] = True

def dfs(graph, stack, visited):
  while len(stack) > 0:
    idx = stack.pop()
    # 인접한 노드들을 탐색한다 
    for j in graph[idx]:
      if visited[j] is not True:
        visited[j] = True
        stack.append(j)
        # 깊이 우선으로 탐색한다. 
        dfs(graph, stack, visited)

dfs(graph, stack, visited)

