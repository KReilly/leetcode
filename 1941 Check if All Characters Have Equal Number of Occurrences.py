class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for item in s:
            if item in d:
                d[item] +=1
            else:
                d[item] =1
        t=d[s[0]]
        for v in d.values():
            if v!=t:
                return False
        return True


s = "abacbc"

#s = "aaabb"
print(Solution.areOccurrencesEqual(Solution, s))