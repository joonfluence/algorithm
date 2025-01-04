# 피연산자 개수 (1~26)
n = int(input())
operands = ['+', '-', '*', '/']
# 후위표현식 (A~Z, 길이는 100 이하)
words = input()
number_inputs = []

stack = []
i = 0

for _ in range(n):
  number_inputs.append(int(input()))

# 숫자는 피연산자가 나오기 전까지 stack 안에 순서대로 값을 담는다
for idx in range(0, len(words)):
  if words[idx].isalpha():
    num = number_inputs[ord(words[idx])-65]
    stack.append(num)
  else:
    i = idx
    break

for element in words[idx:]:
  # 연산자가 나오면 숫자 2개를 pop 해서 계산한다
  if element in operands:
    if len(stack) < 2:
      break
    # 먼저 pop 되는 숫자가 두 번째 값, 나중에 pop되는 숫자가 첫 번째 값으로 하여 계산해야 한다. 계산한 값은 다시 스택에 넣는다
    number2 = stack.pop()
    number1 = stack.pop()
    if element == operands[0]:
      stack.append(number1+number2)
    if element == operands[1]:
      stack.append(number1-number2)
    if element == operands[2]:
      stack.append(number1*number2)
    if element == operands[3]:
      stack.append(number1/number2)
  else:
    stack.append(number_inputs[ord(element)-65])

print(format(stack.pop(), ".2f"))