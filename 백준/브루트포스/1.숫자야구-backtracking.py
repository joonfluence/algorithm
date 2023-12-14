import sys

# 가능한 순열을 저장할 리스트 생성
permu_list= []

# 가능한 모든 순열 구하기
def get_permutations(permu, used):
    global permu_list
    # 3자리 숫자를 만들었을 때, 순열 리스트에 추가하고 종료
    if len(permu) == 3:
        permu_list.append(permu)
        return
    # 사용하지 않은 숫자로 순열을 계속 만듦
    [get_permutations(permu + str(i), used+[i]) for i in range(1,10) if i not in used]

# 처음에 빈 숫자열과 사용한 숫자를 빈 리스트로 get_permutations 함수 호출
get_permutations("", [])

# 입력한 결과에 맞는 가능한 숫자 조합 찾기
def get_results(guess, results):
    can = []
    # 가능한 모든 순열에 대해서
    for p in permu_list:
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