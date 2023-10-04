n, m = list(map(int, input().split()))
numbers = []

for _ in range(n):
    numbers.append(list(map(int, input().split())))

k = int(input())
counters = []

for _ in range(k):
    counters.append(list(map(int, input().split())))

result = []

for counter in counters:
    i, j, x, y = counter
    number_sum = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            number_sum += numbers[a][b]
    result.append(number_sum)

for element in result:
    print(element)
