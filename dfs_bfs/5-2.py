from collections import deque

def bfs(graph, vIdx, visited):
    # deque 객체를 생성한다
    queue = deque([vIdx])
    visited[vIdx] = True
    # 더이상 queue에 값이 없을 때까지 반복한다
    while queue:
        # 그리고 queue에서 제거한다
        v = queue.popleft()
        print(v, end=" ")
        # 방문한 노드와 인접한 노드를 순회하며 queue에 넣는다 
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                # 방문한 노드는 방문처리한다
                visited[v] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)