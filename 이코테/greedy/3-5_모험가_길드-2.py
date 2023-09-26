n = int(input())
fear_list = list(map(int, input().split()))
fear_list.sort()
max_group_count = 0 # 그룹의 최댓값
member_count = 0

print(n, fear_list)

for i in fear_list: # 공포심 목록
    member_count += 1
    if member_count >= i: # 공포 수준보다 멤버 수가 크거나 같을 때
        max_group_count += 1
        member_count = 0

print(max_group_count)