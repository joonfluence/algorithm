def binary_search(array, target, start, end):
  if start > end:
    return print("해당 값은 존재하지 않습니다")
  
  mid = (start + end) // 2
  
  if array[mid] == target:
    print(mid)
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))
# 이진 탐색 수행 결과 출력
binary_search(array, target, 0, n-1)