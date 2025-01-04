n, h = list(map(int, input().split()))
odd = [] # 석순 
even = [] # 종유석 

for idx in range(1, n+1):
  number = int(input())
  if idx % 2 == 0:
    even.append(number)
  else:
    odd.append(number)

odd.sort()
even.sort()

INF = 99999999
obs_cnt = [INF] * (h+1)

# 찾고자 하는 값 이상이 처음 나타나는 인덱스를 반환한다 
def lower_bound(array, target):
  start, end = 0, len(array)

  while start < end:
    mid = (start + end) // 2
    if target <= array[mid]:
      end = mid
    else:
      start = mid + 1
  
  return start

for line in range(1, h+1):
  one = len(odd) - lower_bound(odd, line)
  two = len(even) - lower_bound(even, h - line + 1)
  obs_cnt[line] = one + two
  
print(min(obs_cnt), obs_cnt.count(min(obs_cnt)))
