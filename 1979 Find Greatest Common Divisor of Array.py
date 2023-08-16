from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        gcd = 1
        
        nums.sort()
        l = nums[0]
        h = nums[-1]
        
        for i in range(1,l+1):
            if(l%i ==0 and h%i ==0):
                gcd = i


        return gcd

nums = [2,5,6,9,10]
print(Solution.findGCD(Solution, nums))
