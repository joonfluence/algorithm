n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))
remainders = [0]*m
remainders[0] = 1
total = 0
count = 0

for number in numbers:
    total += number
    idx = total % m
    remainders[idx] += 1

for i in remainders:
    count += i * (i-1) // 2

print(count)
