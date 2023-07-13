n = int(input())
d = [0] * 30001

# top-down, memoization 방식
def dp(x):
  if x == 1:
    return 0
  if d[x] != 0:
    return d[x]

  d[x] = dp(x-1) + 1

  if x % 2 == 0:
    d[x] = min(d[x], dp(x // 2) + 1)
  if x % 3 == 0:
    d[x] = min(d[x], dp(x // 3) + 1)
  if x % 5 == 0:
    d[x] = min(d[x], dp(x // 5) + 1)
  
  return d[x]

print(dp(n))