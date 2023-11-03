a, b = map(int, input().split())
greatest_common_divisor = 1
divider = 2

while (divider <= min(a, b)):
    if a % divider == 0 and b % divider == 0:
        a = a // divider
        b = b // divider
        greatest_common_divisor *= divider
    else:
        divider += 1

print(greatest_common_divisor)
print(a * b * greatest_common_divisor)
