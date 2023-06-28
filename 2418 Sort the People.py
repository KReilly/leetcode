from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        for i in range(len(names)):
            res.append([heights[i],names[i]])
        res = sorted(res,reverse=True)
        return [name for height,name in res]


names = ["Alice","Bob","Bob"]
heights = [155,185,150]

print(Solution.sortPeople(Solution, names, heights))