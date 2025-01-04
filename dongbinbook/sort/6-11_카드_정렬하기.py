import heapq

n = int(input())
heap = []

for _ in range(0, n):
  heapq.heappush(heap, int(input()))

result = 0
print(heap)

while len(heap) > 1:
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  sum_value = one + two
  result += sum_value
  heapq.heappush(heap, sum_value)

print(result)