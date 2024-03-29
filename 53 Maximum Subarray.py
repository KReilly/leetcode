from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)
    

nums = [-2,1,-3,4,-1,2,1,-5,4]

nums = [1]
nums = [5,4,-1,7,8]

print(Solution.maxSubArray(Solution, nums))
 