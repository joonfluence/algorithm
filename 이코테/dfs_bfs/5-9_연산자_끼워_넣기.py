# 수의 갯수
n = int(input())

# 수 목록
numbers = list(map(int, input().split()))

# 연산자 수 목록 (덧셈, 뺄셈, 곱셈, 나눗셈 연산자의 수)
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now): # 1번 호출할 때, 4번 호출됨 
  global min_value, max_value, add, sub, mul, div 
  
  # 숫자를 전부 계산할 때까지
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    if add > 0:
      add -= 1
      dfs(i+1, now+numbers[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i+1, now-numbers[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i+1, now*numbers[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i+1, int(now/numbers[i]))
      div += 1

dfs(1, numbers[0])
print(max_value)
print(min_value)