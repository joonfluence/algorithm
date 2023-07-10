n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(array, target, start, end):
  if start > end:
    return None

  mid = (start + end) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    binary_search(array, target, start, mid - 1)
  else:
    binary_search(array, target, mid + 1, end)

for target in b:
  response = binary_search(a, target, 0, len(a) - 1)
  if response != None:
    print("yes", end=" ")
  else:
    print("no", end=" ")