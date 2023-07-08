# 리스트에 담아 문자열을 각각 구분한다
position = list(input())

# row는 그대로 가져온다 
x_position = int(position[1])

# 문자열(a-h)을 int로 변환한다 
y_position = int(ord(position[0])) - int(ord('a')) + 1

# 이동 가능한 모든 경우의 수 : 8가지
steps = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2), (-2, 1), (-2, -1)]

count = 0
for step in steps:
  # 8가지 경우의 수 중에서 범위 밖인 경우에는 숫자를 세지 않는다
  next_x_position = x_position + step[1]
  next_y_position = y_position + step[0]
  if next_x_position > 1 and next_x_position < 8 and next_y_position > 1 and next_y_position < 8:
    count += 1

print(count)
