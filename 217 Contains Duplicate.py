from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hasDupes = False
        nums.sort()
        prev = pow(10, 9) +10
        for n in nums:
            if(n == prev):
                return True
            prev = n

        return hasDupes

nums = [1,2,3,1]
#nums = [1,2,3,4]
#nums = [1,1,1,3,3,4,3,2,4,2]

print(Solution.containsDuplicate(Solution, nums))