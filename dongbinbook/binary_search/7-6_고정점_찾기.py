n = int(input())
array = list(map(int, input().split()))

def binary_search(array, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if mid == array[mid]:
    return mid
  elif mid < array[mid]:
    return binary_search(array, start, mid-1)
  else:
    return binary_search(array, mid+1, end)

# 이진 탐색(Binary Search) 수행
index = binary_search(array, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
# 고정점이 있는 경우 해당 인덱스 출력
else:
    print(index)