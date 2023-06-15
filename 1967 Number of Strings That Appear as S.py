from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0

        for p in patterns:
            if(word.find(p) != -1):
                count+=1

        return count
    

patterns = ["a","abc","bc","d"]
word = "abc"
print(Solution.numOfStrings(Solution, patterns, word))