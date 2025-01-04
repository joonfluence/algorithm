n = int(input())
position = list(map(int, input().split()))
position.sort()

print(position[(n-1)//2])