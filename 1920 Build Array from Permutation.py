from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            ans.append(nums[n])
        return ans
    

nums = [0,2,1,5,3,4]
print(Solution.buildArray(Solution, nums))


