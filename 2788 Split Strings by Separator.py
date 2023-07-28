from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        sp = []
        for w in words:
            ws = w.split(separator)
            for wss in ws:
                if(wss!=""):
                    sp.append(wss)
        return sp

words = ["one.two.three","four.five","six"]
separator = "."
words = ["$easy$","$problem$"]
separator = "$"
print(Solution.splitWordsBySeparator(Solution, words, separator))