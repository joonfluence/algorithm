# 퀵 정렬 : 피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽에 두는 분할 정렬 방식
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def sort(array, start, end):
  pivot = start # 첫번째 값을 피벗으로 둔다
  left = start + 1
  right = end

  while left <= right:
    # 피벗보다 작은 값을 찾을 때까지 순회한다
    while array[left] <= array[pivot] and left <= end:
      left += 1
    # 피벗보다 큰 값을 찾을 때까지 순회한다
    while array[right] >= array[pivot] and right > start:
      right -= 1
    
    # 엇갈리면 피벗을 교체한다 
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    # 엇갈리지 않았으면 피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽에 두는 swap을 진행한다 
    else:
      array[left], array[right] = array[right], array[left]
  
  # 두 그룹으로 분할하여 정렬함 
  sort(array, start, right - 1)
  sort(array, right+1, end)
  
print(sort(array, 0, len(array)-1))