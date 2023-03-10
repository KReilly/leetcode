from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        last = -101
        c = 0
        for i in range(len(nums)):
            if(last != nums[i]):
                count+=1
                last = nums[i]
                nums[c] = nums[i]
                c+=1
        return count

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(Solution, nums))
print(nums)
