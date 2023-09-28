n = int(input())
time_table = []
count = 0

for _ in range(n):
  time_table.append(list(map(int, input().split())))

time_table.sort(key=lambda x: (x[1], x[0]))
cur_start_time, cur_end_time = (0, 0)

for i in range(0, n):
  start_time, end_time = time_table[i]
  if cur_end_time <= start_time:
    cur_start_time = start_time
    cur_end_time = end_time
    count += 1

print(count)