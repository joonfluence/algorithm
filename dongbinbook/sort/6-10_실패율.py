def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
      count = stages.count(i)
      # 도전한 사용자가 없으면 
      if length == 0:
        fail = 0
      # 실패율 = 현재 도전 중인 수 / 전체 도전자 수 
      else:
        fail = count / length
    
      answer.append((i, fail))
      length -= count
    
    # 실패율이 높은 순서대로 정렬한다 
    answer.sort(key=lambda t: t[1], reverse=True)
    
    # 스테이지만 반환한다 
    return [i[0] for i in answer]

# N : 전체 스테이지 수
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))