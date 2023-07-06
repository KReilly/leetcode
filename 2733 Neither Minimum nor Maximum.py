from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        if len(nums) <=2:
            return -1
        min = nums[0]
        max = nums[0]
        for n in nums:
            if(min > n):
                min = n
            if(max < n):
                max = n
        for n in nums:
            if(n!=min and n!=max):
                return n



nums = [3,2,1,4]
print(Solution.findNonMinOrMax(Solution, nums))