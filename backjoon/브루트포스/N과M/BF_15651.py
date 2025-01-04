"""

풀이과정 

1. N까지의 자연수 중에서 M개를 고른다.
2. 같은 수를 여러 번 골라도 된다. 
3. 고른 수열은 비내림차순이어야 한다. 

"""

N, M = list(map(int, input().split()))
arr = [0] * M

def dfs(depth):
  if depth == M:
    result = ""
    for i in range(0, len(arr)):
      result += str(arr[i]) + " "
    print(result)
    return
  for i in range(1, N+1):
    arr[depth] = i
    dfs(depth+1)

dfs(0)