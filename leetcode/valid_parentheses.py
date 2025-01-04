def isValid(s: str) -> bool:
    stack = []
    opening_brackets = ['(', '{', '[']
    bracket_idx = {
        '(': 0,
        ')': 0,
        '{': 1,
        '}': 1,
        '[': 2,
        ']': 2
    }

    string_list = list(s)
    if len(string_list) <= 1:
        return False

    for bracket in string_list:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if len(stack) > 0 and bracket_idx[stack[-1]] != bracket_idx[bracket]:
                return False
            else:
                if len(stack) > 0:
                    stack.pop()
    
    if len(stack) > 0:
        return False
    
    return True

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("["))
print(isValid("]"))