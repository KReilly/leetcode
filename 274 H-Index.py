from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h = 1
        # citations.sort()

        # for i in range(len(citations)):
            
        #     if(len(citations)-i >= citations[i]):
        #         h = citations[i]
        
        # if(h<citations[0]):


        # return h
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= (n-i):
                return n-i
        return 0


citations = [3,0,6,1,5]
citations = [1,3,1]

print(Solution.hIndex(Solution, citations))