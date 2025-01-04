# 1. 이중 for-loop을 돈다. 
# 2. 돌면서 두 값이 해당 원하는 값과 일치하면 종료한다. 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]