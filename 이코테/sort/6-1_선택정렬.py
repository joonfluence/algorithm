# 선택정렬 대상 
array = [7,5,9,0,3,1,6,2,4,8]

# Swap
def swap(list, pos1, pos2):
  list[pos1], list[pos2] = list[pos2], list[pos1]
  return list

for idx in range(0, len(array)):
  min_value = min(array[idx:])
  min_idx = array.index(min_value)
  if idx != min_idx:
    swap(array, min_idx, idx)

print(array)