n, m = list(map(int, input().split()))
numbers = [[0] * (m+1) for _ in range(n+1)]
psum = [[0] * (m+1) for _ in range(n+1)]

for x in range(1, n+1):
    input_numbers = list(map(int, input().split()))
    for y in range(1, m+1):
        numbers[x][y] = input_numbers[y-1]

for x in range(1, n+1):
    for y in range(1, m+1):
        psum[x][y] = psum[x-1][y] + psum[x][y-1] + numbers[x][y] - psum[x-1][y-1]

k = int(input())
cases = []

for _ in range(k):
    cases.append(list(map(int, input().split())))

for x, y, w, z in cases:
    print(psum[w][z] - psum[x-1][z] - psum[w][y-1] + psum[x-1][y-1])