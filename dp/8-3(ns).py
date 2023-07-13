n = int(input())
foods = list(map(int, input().split()))
d = [0] * 10001

def dp(array, n):
  return d[n - 1]

print(dp(foods, n))
