n = int(input())
# 각 모험가의 공포도의 값이 N 이하로 주어지므로 최소 그룹 수는 1
lists = list(map(int, input().split()))


def greedy_01(n, lists):
  count = 0
  # 공포도가 높은 모험가부터 나열하기 위해, 내림차순 정렬
  lists.sort(reverse=True)

  # 가장 큰 공포도를 가진 사람이 그룹의 수를 결정한다 
  while n > 0:
    max = lists[0]
    
    # n이 max보다 크거나 같으면
    if n >= max:
      count += 1
      # (공포도가 높은 순서대로) 그룹을 지은 인원들을 lists에서 빼준다
      lists = lists[max:]
    
    n -= max
  return count

# 반례 
# 6
# 6 1 1 1 1 1 => 5 
print(greedy_01(n, lists))