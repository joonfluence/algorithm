n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
sum = 0 

for i in range(0, n):
  for j in range(0, i+1):
    sum += numbers[j]

print(sum)