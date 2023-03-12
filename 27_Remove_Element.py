from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert = 0
        count = 0
        for i in range(len(nums)):
            if(val != nums[i]):
                nums[insert] = nums[i]
                count += 1
                insert +=1
        return count


nums = [3,2,2,3]
print(Solution.removeElement(Solution, nums, 3))
print(nums)