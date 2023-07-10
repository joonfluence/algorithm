array = [7, 5, 9, 0, 3, 6, 2, 4, 8]

def selection_sort(array):
    for i in range(len(array)):
        min_index = i # 0번째 값
        for j in range(i + 1, len(array)):
            sliced_array = array[i+1:len(array)] # 나머지 요소와 비교한다
            min_value = min(sliced_array)
            min_index = array.index(min_value)
        
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

print(selection_sort(array))