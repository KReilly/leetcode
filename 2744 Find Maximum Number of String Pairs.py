from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # num = 0
        # w2 = []

        # for w in words:
        #     w2.append(w[::-1])
        # print(words)
        # print(w2)
        
        # for w in words:
        #     for ww in w2:
        #         if(w == ww):
        #             num+=1
        
        # return num
        ans = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if words[i][0] == words[j][1] and words[i][1] == words[j][0]:
                    ans += 1
        return ans


words = ["cd","ac","dc","ca","zz"]
print(Solution.maximumNumberOfStringPairs(Solution, words))