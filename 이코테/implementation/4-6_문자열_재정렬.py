words = list(input())
number_total = 0

for i in words:
  if i.isnumeric(): # 숫자이면
    number_total += int(i)
    words.remove(i) # 리스트에서 제외 

words.sort()
words.append(str(number_total))

result = ""
for i in words:
  result += i

print(result)

# 입력 예시
# 1) K1KA5CB7