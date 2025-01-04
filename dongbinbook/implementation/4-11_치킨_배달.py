from itertools import combinations

# n : 도시크기, m : 치킨집의 최대 갯수
n, m = list(map(int, input().split()))
data = []

for _ in range(1, n+1):
  data.append(list(map(int, input().split())))

# 치킨집 정보
chickens = []
# 도시 정보
houses = []
# 결과
result = []
# 치킨집/도시 위치 초기화
for i in range(0, len(data)):
  for j in range(0, len(data[i])):
    if data[i][j] == 1:
      houses.append((i+1, j+1))
    elif data[i][j] == 2:
      # 최대 갯수가 m 이어야 함
      chickens.append((i+1, j+1)) 

# 치킨집으로부터 집까지의 거리
def calculate(house, chicken):
  r1, c1 = house # 행
  r2, c2 = chicken # 열
  return abs(r1 - r2) + abs(c1 - c2)

s_chickens = list(combinations(chickens, m))

def get_sum(chickens):
  result = 0
  for h in houses: # 6가구
    temp = 1e9
    for c in chickens: # 2개
      distance = calculate(h, c)
      # 집으로부터 치킨 집의 거리
      temp = min(temp, distance)
    result += temp
  return result

result = 1e9
for chickens in s_chickens:
  result = min(result, get_sum(chickens))


# 입력 예시 (1)
# 5 3
# 0 0 1 0 0 
# 0 0 2 0 1
# 0 1 2 0 0 
# 0 0 1 0 0 
# 0 0 0 0 2

# 입력 예시 (2)
# 5 2
# 0 2 0 1 0 
# 1 0 1 0 1
# 0 0 0 0 0 
# 2 0 1 0 1
# 2 2 0 1 2

print(result)