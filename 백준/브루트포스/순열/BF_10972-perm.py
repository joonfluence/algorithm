"""

[풀이과정]

1. 숫자를 그대로 입력 받는다. 
2. 조건을 만족 할 때까지 swap한다. 
3. 자연스럽게 그 다음 순열이 도출된다. 

"""

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
perm = list(map(int, input().split()))

# 순열 계산
permutation = list(permutations(range(1, n+1), n))

# 다음 순열 찾기 
cnt = 0
for idx, i in enumerate(permutation):
  if i == tuple(perm):
    cnt = idx+1

# 마지막 값이면, -1 출력
if cnt == len(permutation):
  print(-1)
# 마지막 값이 아니면 값 출력
else:
  print(" ".join(map(str, permutation[cnt])))