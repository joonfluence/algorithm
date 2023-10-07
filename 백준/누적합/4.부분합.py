n, s = list(map(int, input().split()))
numbers = list(map(int, input().split()))

left = 0
right = 0
number_sum = numbers[0]
min_value = 9999999

while left <= right:
    print(left, right, numbers[left], numbers[right])
    if number_sum < s:
        right += 1
        if right >= n:
          break
        number_sum += numbers[right]
    else:
        min_value = min(min_value, right - left + 1)
        number_sum -= numbers[left]
        left += 1

if min_value == 9999999:
    print(0)
else:
    print(min_value)
