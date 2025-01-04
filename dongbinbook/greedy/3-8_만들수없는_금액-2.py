n = int(input())
numbers = list(map(int, input().split()))

# 오름차순 정렬
numbers.sort()
target = 1

for number in numbers:
  if target < number:
    break
  else:
    target += number

print(target)