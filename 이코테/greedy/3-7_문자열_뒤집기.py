numbers = list(map(int, input()))
count_zero = (1 if numbers[0] == 0 else 0)
count_one = (1 if numbers[0] == 1 else 0)

for i in range(1, len(numbers)):
    previous_num = numbers[i-1]
    current_num = numbers[i]
    if previous_num != current_num:
      if previous_num == 0:
        count_one += 1
      else:  
        count_zero += 1

print(min(count_one, count_zero))