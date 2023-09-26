from itertools import permutations

# 1. 외벽의 길이 n, 취약 지점의 위치를 담은 배열 weak, 각 친구가 이동할 수 있는 거리 정보를 담은 dist를 매개변수로 받는다. 
def solution(n, weak, dist):
  length = len(weak)
  # 2. 원형 리스트를 만들기 위해, weak 배열을 2배로 만든다.   
  for i in range(len(weak)):
    weak.append(weak[i] + n) # 원 초기화
  answer = len(dist) + 1 # 투입할 수의 최솟값을 찾아야 하므로 최댓값으로 설정 
  for start in range(length):
    # 3. 각 친구를 나열하는 모든 경우의 수를 탐색한다. 
    for friends in list(permutations(dist, len(dist))):
      count = 1
      # position = 점검할 수 있는 마지막 위치
      position = weak[start] + friends[count - 1]
      print(weak[start], position, count, friends)
      # 4. 해당 조합으로 시작점부터 끝까지 탐색할 수 있는지 확인한다
      for index in range(start, start+length):
        # 점검할 수 있는 위치를 벗어날 경우
        if position < weak[index]:
          count += 1 # 새로운 친구를 투입한다
          if count > len(dist): # 더 투입할 수 없으면 종료
            break
          position = weak[index] + friends[count - 1]
      answer = min(answer, count) # 최솟값 계산
  # 5. 조회할 수 없다면 -1을 반환한다.
  if answer > len(dist):
    return -1
  return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
