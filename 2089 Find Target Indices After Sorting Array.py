from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        r = []
        nums.sort()
        for i in range(len(nums)):
            if(nums[i] == target):
                r.append(i)

        return r


nums = [1,2,5,2,3]
target = 2
print(Solution.targetIndices(Solution, nums, target))