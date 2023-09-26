numbers = list(map(int, input()))
length = len(numbers)
lucky_straight = False

if sum(numbers[:length//2]) == sum(numbers[length//2:]):
  lucky_straight = True

if lucky_straight:
  print("LUCKY")
else:
  print("READY")