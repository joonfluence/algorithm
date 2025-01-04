import heapq

def solution(food_times, k):
    # 총 음식 식사 시간보다 K가 크면 남은 음식이 없으므로 
    if sum(food_times) <= k:
        return -1
    
    q = [] # 시간이 작은 음식부터 빼야 하므로 우선순위 큐(최소 힙)를 이용 
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # (시간, 인덱스)
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous_eat_time = 0 # 직전에 다 먹은 음식 시간
    rest_food_count = len(food_times) # 남은 음식 수 

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 K 비교
    while sum_value + ((q[0][0] - previous_eat_time) * rest_food_count) <= k:
        current_eat_time = heapq.heappop(q)[0] # 현재 음식을 먹는데 걸리는 시간 
        sum_value += (current_eat_time - previous_eat_time) * rest_food_count
        rest_food_count -= 1 # 다 먹은 음식 제외
        previous_eat_time = current_eat_time # 이전 음식 시간 재설정 
    
    result = sorted(q, key=lambda x: x[1]) # 인덱스 기준으로 정렬 
    return result[(k-sum_value) % rest_food_count][1] # 남은 음식 기준으로 나머지 

solution([3,1,2], 5)