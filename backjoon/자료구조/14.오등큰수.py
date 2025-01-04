from collections import Counter
import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
F = Counter(A) # 미리 세주지 않으면 통과 되지 않음 

answer = [-1] * (N)
stack = []
stack.append(0)

for i in range(1, N):
  # Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수 
  while stack and F[A[stack[-1]]] < F[A[i]]:
    answer[stack.pop()] = A[i]
  stack.append(i)

print(*answer)