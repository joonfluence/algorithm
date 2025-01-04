# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백을 기준으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if target == array[mid]:
    return mid
  # 타겟 값이 중간값보다 작을 때
  elif target < array[mid]:
    return binary_search(array, target, start, mid-1)
  # 타겟 값이 중간값보다 클 때
  else: 
    return binary_search(array, target, mid+1, end)

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  # 해당 부품이 존재하는지 확인
  result = binary_search(array, i, 0, n - 1)
  if result != None:
      print('yes', end=' ')
  else:
      print('no', end=' ')