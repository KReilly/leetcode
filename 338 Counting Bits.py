from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            bitmask = bin(i)[2:]
            out.append(bitmask.count("1"))
            
            
        return out







n=2
n=5

print(Solution.countBits(Solution, n))