from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max = 0
        for n in nums:
            if(n>max):
                max = n
        return k * max + k * (k - 1) // 2; 


nums = [1,2,3,4,5]
k = 3
print(Solution.maximizeSum(Solution, nums, k))