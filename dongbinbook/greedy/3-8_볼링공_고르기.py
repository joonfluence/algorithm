from itertools import combinations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
comb = combinations(numbers, 2) # O(n^2)
count = 0

for i in list(comb):
  x, y = i
  if x != y:
    count += 1

print(count)