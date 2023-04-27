from itertools import combinations
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n+1), k))
    
n = 4 
k = 2

# n = 1
# k = 1
print(Solution.combine(Solution, n, k))
