from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while(high-low >1):
            mid = (high-low)//2 + low
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                high = mid
            elif(nums[mid] < target):
                low = mid 
        mid = (high-low)//2 + low
        if(nums[mid] == target):
            return mid
        else:
            return -1
        

nums = [-1,0,3,5,9,12]
target = 9

# nums = [-1,0,3,5,9,12]
# target = 2

print(Solution.search(Solution, nums, target))