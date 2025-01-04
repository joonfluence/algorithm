# 삽입정렬 대상
array = [7,5,9,0,3,1,6,2,4,8]

# Swap
def swap(list, pos1, pos2):
  list[pos1], list[pos2] = list[pos2], list[pos1]
  return list

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      swap(array, j, j-1)

print(array)