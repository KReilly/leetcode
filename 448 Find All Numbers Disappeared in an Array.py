from typing import List 

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         d = []
#         for n in range(len(nums)):
#             if()
#         print(nums)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


nums = [4,3,2,7,8,2,3,1]
#nums = [1,1]

print(Solution.findDisappearedNumbers(Solution, nums))