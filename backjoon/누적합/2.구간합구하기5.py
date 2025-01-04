n, m = list(map(int, input().split()))
psum = [[0] * (n+1) for _ in range(n+1)]
numbers = []
input_numbers = []

for _ in range(n):
  numbers.append(list(map(int, input().split())))

for _ in range(m):
  input_numbers.append(list(map(int, input().split())))

for i in range(1, n+1):
  for j in range(1, n+1):
    psum[i][j] = psum[i][j-1] + psum[i-1][j] - psum[i-1][j-1] + numbers[i-1][j-1]

result = []

for x, y, z, w in input_numbers:
  print(psum[z][w] - psum[x-1][w] - psum[z][y-1] + psum[x-1][y-1])