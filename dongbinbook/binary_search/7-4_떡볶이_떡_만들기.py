# N(가게의 부품 개수), M(손님이 확인 요청한 부품 개수) 입력
n, m = list(map(int, input().split()))
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))
array = [0] * max(x)

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2 
  result = 0
  for i in x:
    if i > mid:
      result += (i - mid)
  if result == target:
    return mid
  elif result < target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

print(binary_search(array, m, 0, len(array)))