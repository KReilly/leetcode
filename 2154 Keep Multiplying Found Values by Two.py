from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        while(True):
            if(original in nums):
                original *= 2
                print(original)
            else:
                return original



nums = [5,3,6,1,12]
original = 3
print(Solution.findFinalValue(Solution, nums, original))