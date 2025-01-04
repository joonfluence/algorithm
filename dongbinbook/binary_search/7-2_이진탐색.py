# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

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

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)