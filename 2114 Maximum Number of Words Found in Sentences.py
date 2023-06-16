from typing import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # m = 0

        # for s in sentences:


        # return m
        return max(s.count(" ") for s in sentences) + 1

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

print(Solution.mostWordsFound(Solution, sentences))