from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()

        count = 0

        for i in range(len(heights)):
            if(heights[i]!=expected[i]):
                count+=1

        return count



heights = [1,1,4,2,1,3]
print(Solution.heightChecker(Solution, heights))