n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(0, k):
  min_value = min(a)
  min_idx = a.index(min_value)
  max_value = max(b)
  max_idx = b.index(max_value)

  if min_value < max_value:
    a[min_idx] = max_value
    b[max_idx] = min_value

print(sum(a))