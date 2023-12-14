words = input()

# 연산자 우선순위에 따라 정의한다
operands = {'+': 0, '-': 0, '*': 1, '/': 1}
stack = []
result = ''

for word in words:
  if word == '(':
    stack.append(word)
  elif word == ')':
    while stack and stack[-1] != '(':
      result += stack.pop()
    stack.pop()
  else:
    # 숫자라면 그대로 출력한다
    if word not in operands.keys():
      result += word
    # 연산자라면 연산자 우선순위를 비교한다
    else:
      # 만약 스택이 비어있다면 연산자를 그냥 스택에 넣는다
      if len(stack) == 0:
        stack.append(word)
      else:
        if stack[-1] == '(':
          stack.append(word)
        else:
          # 스택의 top에 있는 연산자의 우선순위 >= 현재 연산자의 우선순위이면 스택이 비거나 현재 연산자의 우선순위가 커질 때까지 pop한다 
          if operands.get(stack[-1]) - operands.get(word) >= 0:
            while stack:
              if operands.get(stack[-1]) - operands.get(word) >= 0:
                result += stack.pop()
              else:
                break
            # 연산자를 스택에 넣는다 
            stack.append(word)
          # 스택의 top에 있는 연산자의 우선순위 < 현재 연산자의 우선순위이면 연산자를 그냥 스택에 넣는다
          else:
            stack.append(word)

# 모든 수식을 다 사용했다면 스택이 빌 때까지 pop하여 출력한다.
while stack:
  result += stack.pop()

# 결과를 출력한다 
print(result)