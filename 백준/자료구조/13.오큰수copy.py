import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []

# stack에 첫번째 인덱스를 담는다
stack.append(0)
for i in range(1, n):
  # 인접한 두 원소 중 오른쪽이 클 때, stack을 pop하여 answer를 업데이트한다. 
  # stack이 비거나 왼쪽의 값이 더 큰 값을 가질 때까지 반복한다.
  while stack and A[stack[-1]] < A[i]:
    answer[stack.pop()] = A[i]
  # stack의 가장 위에 있는 값이 현재 오른쪽 값보다 작은 지 확인하고, 작다면 pop 한다
  stack.append(i)

print(*answer)