n = input()
m = n.split('-')
answer = 0

x = sum(map(int, m[0].split('+')))
answer += x

for x in m[1:]:
  x = sum(map(int, x.split('+')))
  answer -= x

print(answer)