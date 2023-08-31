from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(c in allowed for c in w) for w in words)



allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(Solution.countConsistentStrings(Solution, allowed, words))