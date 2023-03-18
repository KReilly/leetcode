class Solution:
    def mySqrt(self, x: int) -> int:
        last = 0
        for i in range(0,46344):
            sqi = i*i
            if(x == sqi):
                return i
            if(x < sqi):
                return last
            last = i
        return -1
    




x = 8
print(Solution.mySqrt(Solution, x))