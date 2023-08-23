from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = edges[0]
        b = edges[1]
        for i in a:
            for j in b:
                if(i==j):
                    return i
                
edges = [[1,2],[2,3],[4,2]]
print(Solution.findCenter(Solution, edges))