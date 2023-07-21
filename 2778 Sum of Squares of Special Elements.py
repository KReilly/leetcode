from typing import List
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum = 0
        l = len(nums)
        for i in range(l):
            if(l%(i+1) == 0):
                sum += nums[i]*nums[i]


        return sum


nums = [1,2,3,4]
nums = [2,7,1,19,18,3]

print(Solution.sumOfSquares(Solution, nums))