n, m = map(int, input().split())
numbers = list(map(int, input().split()))
input_values = []
result = []
psum = [0] * (n+1)
psum[1] = numbers[0]

for _ in range(m):
  input_values.append(list(map(int, input().split())))

for i in range(2, len(numbers)+1):
  psum[i] = psum[i-1] + numbers[i-1]

for value in input_values:
  start, end = value
  number_sum = 0
  
  if start == 1:
    result.append(psum[end])
  else:
    result.append(psum[end] - psum[start-1])

for element in range(len(result)):
  print(result[element])