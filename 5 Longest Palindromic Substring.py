#weird error where you need to define self, but not pass it on leetcode, but need to pass it locally

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(s == ""):
            return ""
        end = 0
        start = 0
        for i in range(0,len(s)):
             a = self.expand(s,i,i)
             b = self.expand(s,i,i+1)
             c = max(a,b)
             if(c > end - start):
                end = i + int(c/2)
                start = i - int((c-1)/2)
        return s[start: end+1]
    
    def expand(self, s: str, i:int, j:int) -> int:
        l = i
        r = j
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            l-=1
            r+=1
        return r-l -1
    

s = "babad"
#s = "cbbd"

print(Solution.longestPalindrome(Solution, s))

