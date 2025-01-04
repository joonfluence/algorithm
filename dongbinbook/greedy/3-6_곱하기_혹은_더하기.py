numbers = list(map(int, input()))
max_result = 0

for i in range(0, len(numbers)):
  # 피연산자가 0과 1이 아닌 이상, 곱한다
  if numbers[i] == 0 or numbers[i] == 1 or max_result == 0:
    max_result += numbers[i]
  else:
    max_result *= numbers[i]

print(max_result)