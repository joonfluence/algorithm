def posibble(answer):
  for x, y, structure in answer:
    if structure == 0: # 기둥
      # 바닥 위 or 보의 한쪽 끝부분(왼쪽, 오른쪽) 위 or 다른 기둥 위
      if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer: 
        continue
      else:
        return False
    elif structure == 1: # 보
      # 한쪽 끝 부분(왼쪽, 오른쪽)이 기둥 위 or 양쪽 끝 부분이 다른 보와 연결된 경우
      if [x+1, y-1, 0] in answer or [x, y-1, 0] in answer or ([x-1, y, 1] and [x+1, y, 1] in answer):
        continue
      else:
        False
  return True

def solution(n, build_frame):
  answer = []
  for frame in build_frame:
    x, y, structure, action = frame
    if action == 0: # 삭제
      answer.remove([x, y, structure])
      if not posibble(answer) == True:
        answer.append([x, y, structure]) # 삭제할 수 없다면 되돌린다
    elif action == 1: # 추가
      answer.append([x, y, structure])
      if not posibble(answer) == True: # 추가할 수 없다면 되돌린다
        answer.remove([x, y, structure])
  return sorted(answer)

# 예제 1
print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))

# 예제 2
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))