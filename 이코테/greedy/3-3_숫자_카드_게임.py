# 숫자 카드 게임 

n, m = map(int, input().split())
numbers = []
for _ in range(n):
  numbers.append(input().split() )

min_num_list = []
for i in range(0, len(numbers)):
  min_num_list.append(min(numbers[i]))

print(max(min_num_list))