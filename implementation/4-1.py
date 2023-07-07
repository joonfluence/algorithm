n = int(input())
actions = list(input().split())

def implementation():
  current_position = [1, 1]
  current_position_y = current_position[0]
  current_position_x = current_position[1]

  while len(actions) > 0:
    mover = actions.pop(0)

    # x 축으로 이동시킨다
    if mover == 'R':
      if current_position_x < n:
        current_position_x += 1
    elif mover == 'L':
      if current_position_x > 1:
        current_position_x -= 1
    
    # y 축으로 이동시킨다
    if mover == 'U':
      if current_position_y > 1:
        current_position_y -= 1
    elif mover == 'D':
      if current_position_y < n:
        current_position_y += 1
  
  result = str(current_position_y) + " " + str(current_position_x)
  print(result)

implementation()
