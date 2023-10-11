n = int(input())
actions = input().split()
x, y = 1, 1

moves = ['L', 'R', 'U', 'D']
moves_action = [(0, -1), (0, 1), (-1, 0), (1, 0)]

for action in actions:
    nx, ny = 0, 0
    for moveIdx in range(0, len(moves)):
        if action == moves[moveIdx]:
            dx, dy = moves_action[moveIdx]
            nx = x + dx
            ny = y + dy
            if nx <= n and nx > 0 and ny <= n and ny > 0:
                x = nx
                y = ny
            break

print(x, y)
