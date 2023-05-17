class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            st = s[i:] + s[0:i]
            print(st)
            if(st == goal):
                return True
            
        return False



s = "abcde"
goal = "cdeab"
s = "abcde"
goal = "abced"
print(Solution.rotateString(Solution, s, goal))