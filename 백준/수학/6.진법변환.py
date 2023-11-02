words, b = input().split()
b = int(b)
ans = 0
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(0, len(words)):
  ans += b**(len(words)-1-i) * chars.find(words[i])

print(ans)