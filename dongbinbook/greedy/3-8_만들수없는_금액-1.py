from itertools import combinations

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
makable = [] # 만들 수 있는 수의 목록 

for count in range(1, n+1):
  comb = combinations(numbers, count) # O(n^2)
  for i in list(comb): # O(n)
    makable_num = sum(i) 
    if makable_num not in makable: 
      makable.append(makable_num) 

makable.sort()
print(makable)

for i in range(1, 1000000):
  if i not in makable:
    print(i)
    break
