# N : 배열의 크기
# M : 숫자 더하는 횟수
# K : 연속횟수

n, m, k = list(map(int, input().split()))
numbers = sorted(list(map(int, input().split())))
max_num = numbers[-1]
second_max_num = numbers[-2]

def greedy():
  sum = 0
  count = 0
  max_sum_count = 0
  is_max_sum_ok = True

  # count < m보다 작고 가장 큰 수를 더한 횟수가 k보다 작으면 가장 큰 수를 더한다. 
  while count < m:
    count += 1
    if is_max_sum_ok:
      sum += max_num
      max_sum_count += 1
      if max_sum_count >= k:
        is_max_sum_ok = False
    # count < m보다 작고 가장 큰 수를 더한 횟수가 k보다 크면 두번쨰로 작은 수를 더한다.
    else:
      sum += second_max_num
      is_max_sum_ok = True
      max_sum_count = 0
  
  return sum

sum = greedy()
print(sum) 
