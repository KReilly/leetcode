from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0

        for w in words:
            if(len(w)<=len(s) and w == s[:len(w)]):
                count+=1


        return count
    

words = ["a","b","c","ab","bc","abc"]
s = "abc"
print(Solution.countPrefixes(Solution, words, s))