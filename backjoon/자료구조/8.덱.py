from collections import deque

n = int(input())
input_values = []
deck = deque()

for _ in range(n):
  input_values.append(input().split())

for value in input_values:
  if value[0] == 'pop_front':
    if deck:
      print(deck.popleft())
    else:
      print(-1)
  elif value[0] == 'pop_back':
    if deck:
      print(deck.pop())
    else:
      print(-1)
  elif value[0] == 'push_back':
    deck.append(int(value[1]))
  elif value[0] == 'push_front':
    deck.appendleft(int(value[1]))
  elif value[0] == 'front':
    if deck:
      print(deck[0])
    else:
      print(-1)
  elif value[0] == 'back':
    if deck:
      print(deck[len(deck)-1])
    else:
      print(-1)
  elif value[0] == 'size':
    print(len(deck))
  elif value[0] == 'empty':
    if deck:
      print(0)
    else:
      print(1)
