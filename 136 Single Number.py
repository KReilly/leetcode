from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            x ^= i
        return x


nums = [2,2,1]
nums = [4,1,2,1,2]
#nums = [1]

print(Solution.singleNumber(Solution, nums))