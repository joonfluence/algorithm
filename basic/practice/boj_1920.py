# 이진탐색 연습문제

N = int(input())
n_numbers = sorted(list(map(int, input().split())))
M = int(input())
m_numbers = list(map(int, input().split()))

def binary_search(target, start, end, list):
    if start > end:
        return print(0)
    
    mid = (start + end) // 2
    if target == list[mid]:
        return print(1)
    
    if target < list[mid]:
        binary_search(target, start, mid-1, list)
    else:
        binary_search(target, mid+1, end, list)

for m in m_numbers:
    binary_search(m, 0, len(n_numbers)-1, n_numbers)