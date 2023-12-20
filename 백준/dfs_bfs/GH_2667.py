import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = []  # 입력받을 그래프를 담을 리스트 선언
result = []  # 결과를 담을 리스트 선언

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    queue = deque()  # 큐 선언
    queue.append([a, b])  # a ,b 를 큐에서 그대로 빼기 위해 append로 추가를 해준다.
    graph[a][b] = 0  # 첫번째 집 a,b를 방문 처리해준다.
    count = 1  # 첫번째 집 a,b 를 방문했기 때문에 count값을 1로 시작한다.
    
    while queue:
        x, y = queue.popleft()  # 큐에 들어간 좌표 x,y를 파이썬 문법을 활용하여 그대로 빼준다.
        graph[x][y] = 0
        for i in range(4):  # 각 좌표마다 위 아래 왼쪽 오른쪽으로 이동
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표를 이동했는데 그래프 범위를 벗어 나는 경우
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue

            if graph[nx][ny] == 1:  # 만약 1이라면(집을 방문을 안했다면)
                graph[nx][ny] = 0  # 방문했던 곳은 0으로 만들어 버린다.
                queue.append([nx, ny])  # 새로운 x ,y 좌표를 큐에 추가
                count += 1  # count값 1 증가

    return count


# 그래프의 원소가 1일때 bfs로 집을 방문한다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
            result.append(count)

result.sort()  # 오름차순으로 정렬

print(len(result))  # 총 단지수 출력
for k in result:  # 각 단지마다 집의 수 출력
    print(k)