from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zcnt = 0
        for n in nums:
            if(n == 0):
                zcnt +=1
        

nums = [0,1,0,3,12]
#nums = [0]

Solution.moveZeroes(Solution, nums)
print(nums)
