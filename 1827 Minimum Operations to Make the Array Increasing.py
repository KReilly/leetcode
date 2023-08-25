from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        prev = nums[0]-1

        for n in nums:
            if(n<=prev):
                ops += prev-n +1
                prev += 1
            else:
                prev = n


        return ops
    
nums = [1,1,1]
nums = [1,5,2,4,1]
print(Solution.minOperations(Solution, nums))