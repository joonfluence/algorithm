n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))
idx = k
total = sum(numbers[:idx])
answer = total

while idx < n:
  total += numbers[idx] - numbers[idx-k]
  if answer < total:
    answer = total
  idx += 1
  
print(answer)

