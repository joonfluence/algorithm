S = list(input())
stack = []
i = 0
start = 0

while i < len(S):
    if S[i] == '<':
      i += 1
      while S[i] != '>':
        i += 1
      i += 1
    elif S[i].isalnum():
      start = i
      while i < len(S) and S[i].isalnum():
         i += 1
      temp = S[start:i]
      temp.reverse()
      S[start:i] = temp
    else:
       i+=1

print("".join(S))