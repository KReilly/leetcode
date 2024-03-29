from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: 
                return [d[r], i]
            d[j] = i


nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

print(Solution.twoSum(Solution, nums, target))