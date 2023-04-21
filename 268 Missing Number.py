from typing import List 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if(i != nums[i]):
                return i
        return len(nums)

nums = [3,0,1]
nums = [0,1]
#nums = [9,6,4,2,3,5,7,0,1]

print(Solution.missingNumber(Solution, nums))