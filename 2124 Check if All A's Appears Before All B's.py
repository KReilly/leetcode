

class Solution:
    def checkString(self, s: str) -> bool:
        flag = True

        for c in s:
            if flag and c =="b":
                flag = False
            elif not flag and c == "a":
                return False
        
        return True



s = "abab"
#s = "aaabbb"
#s = "bbbbb"

print(Solution.checkString(Solution, s))