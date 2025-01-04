from collections import deque

n = int(input())
input_values = []
queue = deque()
for _ in range(n):
    input_values.append(input().split())

for value in input_values:
    if value[0] == 'pop':
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif value[0] == 'push':
        queue.append(int(value[1]))
    elif value[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif value[0] == 'back':
        if len(queue) > 0:
            print(queue[len(queue)-1])
        else:
            print(-1)
    elif value[0] == 'size':
        print(len(queue))
    elif value[0] == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
