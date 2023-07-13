n, m = map(int, input().split())
# 캐릭터의 현재 위치와 방향
x, y, direction = map(int, input().split())
d = []

# 방문정보 0으로 초기화, 방문하면 1 할당
for _ in range(n):
  d.append([0] * m)

print(d)
d[x][y] = 1

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 순서대로 : 좌 하 우 상
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1] 