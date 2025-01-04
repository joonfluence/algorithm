import bisect

t = int(input())
n = int(input())
n_number = list(map(int, input().split()))
m = int(input())
m_number = list(map(int, input().split()))

n_numbers, m_numbers = [], []
for i in range(n):
    for j in range(i+1, n+1):
        n_numbers.append(sum(n_number[i:j]))
for i in range(m):
    for j in range(i + 1, m + 1):
        m_numbers.append(sum(m_number[i:j]))

n_numbers.sort()
m_numbers.sort()

ans = 0
for i in range(len(n_numbers)):
    bmp = t - n_numbers[i]
    left = bisect.bisect_left(m_numbers, bmp)
    right = bisect.bisect_right(m_numbers, bmp)
    ans += (right - left)

print(ans)
