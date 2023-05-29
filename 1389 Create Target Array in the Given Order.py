from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            final.insert(index[i], nums[i])
        return final

    
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
# nums = [1,2,3,4,0]
# index = [0,1,2,3,0]
# nums = [1]
# index = [0]

print(Solution.createTargetArray(Solution, nums, index))