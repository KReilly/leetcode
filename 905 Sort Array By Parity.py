from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e = []
        odd = []

        for n in nums:
            if(n%2 == 0):
                e.append(n)
            else:
                odd.append(n)
        for o in odd:
            e.append(o)

        return e




nums = [3,1,2,4]
#nums = [0]

print(Solution.sortArrayByParity(Solution, nums))