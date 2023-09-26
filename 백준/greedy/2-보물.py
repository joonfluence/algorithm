n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()
sum = 0

for i in range(len(a)):
  sum += a[i] * b[i]

print(sum)