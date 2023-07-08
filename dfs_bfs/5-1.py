# 그래프를 초기화한다
graph = [[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]] # 인접리스트 방식

# 각 노드의 방문 정보를 리스트에 저장한다 
visitedArr = [False] * 9

def dfs(graph, visitIdx, visitedArr):
  # 방문한 곳은 방문 처리한다
  visitedArr[visitIdx] = True
  # 방문한 요소는 출력한다 
  print(visitIdx, end=" ")
  # 인접한 노드들을 쭉 탐색한다 
  for nearIdx in graph[visitIdx]:
    if not visitedArr[nearIdx]:
      dfs(graph, nearIdx, visitedArr)

dfs(graph, 1, visitedArr)