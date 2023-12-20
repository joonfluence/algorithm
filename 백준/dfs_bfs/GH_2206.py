"""
https://www.acmicpc.net/problem/2206
https://data-flower.tistory.com/85

0: 이동가능, 1: 벽
이동가능 -> 상하좌우

풀이과정

1. maps, N, M 등 필요한 값들을 입력 받는다. 

"""

N, M = list(map(int, input().split()))
maps = [list(map(int, list(input()))) for _ in range(N)]
moves = [{0, 1}, {0, -1}, {1, 0}, {-1, 0}]
print(maps)

