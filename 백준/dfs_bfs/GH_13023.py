import io
import sys

def test_code(input_string):
    # Mock the input
    sys.stdin = io.StringIO(input_string)

    # Your existing code goes here
    n, m = list(map(int, input().split()))
    relations = [[] for _ in range(n)]
    visited = [False] * 2001
    ans = False

    for _ in range(m):
        a, b = list(map(int, input().split()))
        relations[a].append(b)
        relations[b].append(a)

    def dfs(idx, depth):
        nonlocal ans
        visited[idx] = True
        if depth == 4:
            ans = True
            return
        for i in relations[idx]:
            if not visited[i]:
                visited[i] = True
                dfs(i, depth + 1)
                visited[i] = False

    for i in range(n):
        dfs(i, 0)
        visited[i] = False
        if ans:
            break

    if ans:
        print(1)
    else:
        print(0)

# Test input
input_string = """5 4
0 1
1 2
2 3
3 4
"""

input_string4 = """5 5
0 1
1 2
2 3
3 0
1 4
"""

input_string2 = """6 5
0 1
0 2
0 3
0 4
0 5
"""


input_string1 = """8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7
"""

# Run the test
test_code(input_string)
test_code(input_string4)
test_code(input_string2)
test_code(input_string1)
