d = [0] * 100

# top-down, memoization 방식
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  
  if d[n] != 0:
    return d[n]
  
  d[n] = fibonacci(n - 1) + fibonacci(n - 2)
  return d[n]

print(fibonacci(99))