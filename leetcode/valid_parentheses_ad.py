def isValid(s: str) -> bool:
        stack = []  # 스택 초기화
        mapping = {')': '(', '}': '{', ']': '['}  # 닫는 괄호와 여는 괄호 매핑

        for char in s:
            if char in mapping:  # 닫는 괄호인 경우
                top_element = stack.pop() if stack else '#'  # 스택에서 pop, 비어 있으면 # 반환
                if mapping[char] != top_element:  # 짝이 맞지 않으면 False
                    return False
            else:
                stack.append(char)  # 여는 괄호는 스택에 push

        return not stack  # 스택이 비어 있으면 True

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("["))
print(isValid("]"))