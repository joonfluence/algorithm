n = int(input())
nums = []

for n in range(n):
  nums.append(input())

sortedNums = sorted(nums, reverse=True)
print(sortedNums, end=" ")