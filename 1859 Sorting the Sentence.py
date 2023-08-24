class Solution:
    def sortSentence(self, s: str) -> str:
        sp = s.split(" ")
        out = sp.copy()
        
        for ws in sp:
            index = int(ws[-1])
            word = ws[0:len(ws)-1]
            out[index-1] = word + " "
        ret = ""
        for a in out:
            ret += a
        return ret[0:len(ret)-1]




s = "is2 sentence4 This1 a3"
print(Solution.sortSentence(Solution, s))