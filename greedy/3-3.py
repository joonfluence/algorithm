def greedy():
  n, m = list(map(int, input().split()))
  min_num = 0

  for n in range(n):  
    numbers = sorted(list(map(int, input().split())))
    
    if n == 0:
      min_num = numbers[0]
    else:
      if min_num < numbers[0]:
        min_num = numbers[0]
  
  return min_num

res = greedy()
print(res)