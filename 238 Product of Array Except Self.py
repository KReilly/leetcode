from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first = []
        #first.append(1)
        p=1             
        last = []
        for i in range(len(nums)):
            first.append(p)
            p = nums[i]*p
        
        l = 1
        for i in range(len(nums)):
            j = len(nums) - i -1
            #j = i
            last.append(l)
            l = nums[j]*l
        last.reverse()

        final = []
        for i in range(len(nums)):
            final.append(first[i]*last[i])

        return final
    
nums = [1,2,3,4]
#nums = [-1,1,0,-3,3]

print(Solution.productExceptSelf(Solution, nums))