def solution(s):
  length = len(s)
  answer = length
  # 1. 문자 압축 단위를 1부터 최대 주어진 문자열의 절반 크기까지 순회한다. 
  for step in range(1, length // 2 + 1):
    compressed = ""
    count = 1
    # 2. 각 압축 단위로 계산했을 때, 문자의 연속된 횟수를 파악한다. 
    for i in range(step, length, step):
      # divider가 1일 떄
      prev = s[i-step:i]
      current = s[i:i+step]
      # 3. 연속된 횟수만큼 숫자를 계산해, 문자열 형태로 반환한다. 
      if prev == current:
        count += 1
      else:
        compressed += str(count) + prev if count >= 2 else prev
        prev = current # 다시 상태 초기화
        count = 1
    compressed += str(count) + prev if count >= 2 else prev
    # 4. 압축된 문자열이 가장 작은 경우를 출력한다. 
    answer = min(answer, len(compressed))
  return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))