n = int(input())
array = []

for _ in range(0, n):
  nm, k, e, m = input().split()
  array.append((nm, int(k), int(e), int(m)))

# 국 -> 영 -> 수 순서대로 정렬
array.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in array:
  print(student[0])