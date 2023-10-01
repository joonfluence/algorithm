mushrooms = []
psum = [0] * 11
number_sum = 0
result = []

for _ in range(10):
  mushrooms.append(int(input()))

for i in range(10):
  number_sum += mushrooms[i]
  psum[i+1] = number_sum

for i in range(0, len(psum)):
  result.append((abs(psum[i]-100), i))

result = list(filter(lambda x: x[0] == min(result)[0], result))
_, idx = max(result)
print(psum[idx])
