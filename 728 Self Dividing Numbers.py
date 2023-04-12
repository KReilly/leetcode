from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for n in range(left, right+1):
            m = n
            isDividing = True
            while(m > 0):
                d = m%10
                if(d == 0):
                    isDividing = False
                    break
                if(n%d != 0):
                    isDividing = False
                m = m//10
            if(isDividing):
                l.append(n)



        return l
    

left = 1
right = 22

left = 47
right = 85

print(Solution.selfDividingNumbers(Solution, left, right))
