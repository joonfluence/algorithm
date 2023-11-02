n, b = list(map(int, input().split()))
ans = ''
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n != 0:
    ans += chars[n % b]
    n = n // b

print(ans[::-1])
