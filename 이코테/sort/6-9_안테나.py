n = int(input())
position = list(map(int, input().split()))
map = [0] * (max(position) + 1)
d = [0] * (max(position) + 1)
print(d)

# 안테나 위치정보 
antena = 0

# 1. 각 위치에 안테나를 설치한다.
for idx in range(1, len(map)):
  for element in position:
    # 2. 각 경우의 거리의 합을 구한다. 
    d[idx] += abs(element - idx)

# 3. 0번쨰 인덱스를 제외하고, 그 중 가장 작은 값을 도출한다. 
print(d.index(min(d[1:])))