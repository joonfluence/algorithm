# 큰 수의 법칙

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
max_num = numbers[-1]
second_max_num = numbers[-2]

count = 0 # 반복 횟수
max_num_count = 0 # 최댓값 카운트 횟수 
sum = 0 # 결괏값s

# 가장 큰 수를 K번 연속으로 더하고 두번쨰로 큰 수를 1번 더한다
while count < m:
  if max_num_count >= k:
   sum += second_max_num
   max_num_count = 0
  else:
    sum += max_num
    max_num_count += 1
  # 한번 더한다
  count += 1

print(sum)