from collections import deque

n, k = list(map(int, input().split()))
idx = k-1
numbers = []

for i in range(1, n+1):
    numbers.append(i)

queue = deque(numbers)
count = 1
results = []

# 큐가 빌 때까지 반복한다
while queue:
    if count == k:
        results.append(queue.popleft())
        count = 1
    else:
        queue.append(queue.popleft())
        count += 1

print('<', end='')
for idx in range(0, len(results)):
    if idx == len(results)-1:
        print(results[idx], end="")
    else:
        print(results[idx], end=", ")
print('>', end='')