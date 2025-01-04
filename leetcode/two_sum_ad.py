# 1. HashTable 안에 해당 값과 인덱스를 저장
# 2. for-loop 돌면서 원하는 값(target-num)이 HashTable 안에 존재하는지 확인

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_idx:
                return [num_to_idx[complement], i]
            num_to_idx[num] = i