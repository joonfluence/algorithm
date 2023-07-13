n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    return 0

result = 0
for i in range(n):
    for j in range(m):
        # 전부 탐색
        if dfs(i, j) == True:
            result += 1

print(result)