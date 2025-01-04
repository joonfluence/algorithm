n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))

left, right = 0, 1
count = 0

while left <= right and right <= n:
    total = sum(numbers[left:right])

    if total == m:
        count += 1
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1

print(count)
