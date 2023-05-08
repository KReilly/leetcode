from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(len(nums)):
            if(i%2==0):
                sum += nums[i]


        return sum

nums = [1,4,3,2]
nums = [6,2,6,5,1,2]

print(Solution.arrayPairSum(Solution, nums))