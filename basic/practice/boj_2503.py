from itertools import permutations

N = int(input())
data = []

# 1. 가능한 조합 구하기
def get_possible_results(guess, results):
  can = []

  # 가능한 조합 모두 찾기
  for p in permutations('123456789', 3):
    strike = sum(p[i] == guess[i] for i in range(3))
    ball = sum(guess[i] in p for i in range(3)) - strike
    if results == (strike, ball):
       can += [p]

  return can

# 2. 주어진 입력을 받는다. 
result = []
for _ in range(0, N):
    guess, strike, ball = map(int, input().split())
    can = get_possible_results(str(guess), (strike, ball))
    # 초기화 해준다. 
    if result == []:
       result = can
    else:
       result = [c for c in can if c in result] # 기존에 있는 조합과 일치하는 것만 뽑는다

# 3. 가능한 조합의 개수 출력
print(len(result))