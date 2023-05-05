from typing import List 

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)


nums = [4,3,2,7,8,2,3,1]
#nums = [1,1]

print(Solution.findDisappearedNumbers(Solution, nums))