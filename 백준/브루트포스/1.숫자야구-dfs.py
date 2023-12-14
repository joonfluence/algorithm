import sys
from itertools import permutations

# 입력한 결과에 맞는 가능한 숫자 조합 찾기 
def get_results(guess, results):
  can = []
  # 가능한 모든 순열에 대해서
  for p in permutations('123456789', 3):
    # 스트라이크 개수 계산
    strike = sum(p[i] == guess[i] for i in range(3))
    # 볼 개수 계산
    ball = sum(guess[i] in p for i in range(3)) - strike
    # 결과가 맞는 경우 가능한 조합 리스트에 추가
    if results == (strike, ball):
      can += [p]
  return can

# 모든 입력 결과에 대해 가능한 조합 리스트를 구하고, 이전 입력 결과에서 가능한 조합과 겹치는 것만 result 리스트에 남김
result = []
for _ in range(int(input())):
    guess, strike, ball = map(int,sys.stdin.readline().split())
    can = get_results(str(guess), (strike, ball))
    # result 리스트가 비어있으면, 가능한 조합 리스트 전체를 result 리스트로 할당
    if result == []:
        result = can
    # result 리스트가 비어있지 않으면, 가능한 조합 리스트 중 이전에 구한 가능한 조합 리스트에도 포함된 것만 남김
    else:
        result = [c for c in can if c in result]

# 가능한 조합의 개수 출력
print(len(result))