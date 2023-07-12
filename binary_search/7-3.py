# 리팩토링 필요

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

def binary_search(array, target, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2
  new_list = list(map(lambda x: x - mid, a))
  sum_of_list = 0

  for i in new_list:
    if i > 0:
      sum_of_list += i
  if sum_of_list == target:
    print(mid)
    return mid
  elif sum_of_list < target:
    binary_search(array, target, start, mid-1)
  else:
    binary_search(array, target, mid+1, end)

result = binary_search(a, m, 0, a[-1])
if result != None:
  print(result)
else:
  print("값이 존재하지 않습니다")