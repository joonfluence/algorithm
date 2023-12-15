"""

[풀이과정]

1. 숫자를 그대로 입력 받는다. 
2. ~ 할 때까지 swap한다.
3. 자연스럽게 그 다음 순열이 도출된다. 

"""

import sys
input = sys.stdin.readline

N = int(input())
perm = list(map(int, input().split()))

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

# 맨 뒤부터 탐색
for i in range(N-1, 0, -1):
  # 뒤 값보다 앞 값이 더 크면
  if perm[i-1] < perm[i]:
    # 다시 뒤에서부터, 앞 값보다 큰 값이 있는지 탐색한다.
    for j in range(N-1, 0, -1):
      # 뒤 값이 앞 값보다 크면
      if perm[i-1] < perm[j]:
        # 두 값을 swap
        swap(perm, i-1, j)
        perm = perm[:i] + sorted(perm[i:])
        print(" ".join(map(str, perm)))
        exit()

# 만약 뒷 값이 앞 값보다 큰 경우가 없다면, 맨 마지막 순열이므로 -1 출력
print(-1)