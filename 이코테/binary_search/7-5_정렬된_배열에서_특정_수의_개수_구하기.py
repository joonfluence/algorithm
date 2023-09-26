from bisect import bisect_left, bisect_right

def count_range(array, left_value, right_value):
  left_idx = bisect_left(array, left_value)
  right_idx = bisect_right(array, right_value)
  return right_idx - left_idx

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력 받기
count = count_range(array, x, x) # count 횟수 

if count == 0:
  print(-1)
# 값이 x인 원소가 존재한다면
else:
  print(count)