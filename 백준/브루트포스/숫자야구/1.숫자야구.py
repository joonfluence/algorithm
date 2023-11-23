# 입력 값을 초기화해준다 
n = int(input())
numbers = []

for _ in range(n):
  numbers.append(list(map(int, input().split())))

for element in numbers:
  num, s, b = element
  print(num, s, b)

# 완전 탐색한다.
for a in range(1, 10):
  for b in range(1, 10):
    for c in range(1, 10):
      # 조건에 맞는 수를 찾는다
      if a == 0:
        print(a,b,c)

