from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        l = 0
        r = 1
        while r < len(prices):
            p = prices[r] - prices[l]
            if(prices[l] < prices[r]):
                m = max(m, p)
            else:
                l = r
            r +=1


        return m
    
prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]

print(Solution.maxProfit(Solution, prices))