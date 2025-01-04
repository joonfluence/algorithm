def check(new_lock):
  lock_length = len(new_lock) // 3
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1:
        return False
  return True

def rotate_a_matrix_by_90(key):
  n = len(key) # 행 길이 
  m = len(key[0]) # 열 길이 
  new_key = [[0] * n for _ in range(m)] # 새로운 결과 리스트를 생성한다
  for i in range(n):
    for j in range(m):
      row = j
      column = n-i-1
      new_key[row][column] = key[i][j]
  return new_key

def solution(key, lock):
  # 1. 2차원 배열 key와 자물쇠를 나타내는 배열 lock을 매개변수로 받아, x3 버젼 새로운 자물쇠에 넣는다.
  m = len(key)
  n = len(lock)
  new_lock = [[0] * (n*3) for _ in range(n * 3)]
  for i in range(n):
    for j in range(n):
      new_lock[i+n][j+n] = lock[i][j]

  # 2. 열쇠를 회전해서 돌기를 제거할 수 있는가?
  for _ in range(4):
    key = rotate_a_matrix_by_90(key)
    for x in range(n * 2):
      for y in range(n * 2):
        for i in range(m): 
          for j in range(m): 
            new_lock[x+i][y+j] += key[i][j]
        # 3. 열쇠를 이동해서 열쇠 영역의 돌기가 자물쇠 영역의 돌기에서 벗어나게 할 수 있는가?
        if check(new_lock) == True:
          return True
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+j] -= key[i][j]
  
  # 5. 그렇게 할 수 있으면 True, 없으면 False를 반환한다. 
  return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))