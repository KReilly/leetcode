class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
    
nums = [3,2,3]
#nums = [2,2,1,1,1,2,2]

print(Solution.majorityElement(Solution, nums))