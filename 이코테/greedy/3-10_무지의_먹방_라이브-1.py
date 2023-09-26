def solution(food_times, k):
    answer = 0
    while k >= 0:
        if max(food_times) == 0:
            return -1
        for i in range(0, len(food_times)):
          if food_times[i] == 0:
              continue
          if k == 0 and food_times[i] > 0:
              answer = i+1
              return answer
          food_times[i] = food_times[i] - 1
          k -= 1
    return answer