from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if(nums[i]-nums[j] == k or nums[j]-nums[i] == k):
                    c+=1



        return c
    

nums = [1,2,2,1]

k = 1

print(Solution.countKDifference(Solution, nums, k))