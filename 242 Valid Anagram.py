class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))
        if(t1 == s1):
            return True
        else:
            return False
        
s = "anagram"
t = "nagaram"

print(Solution.isAnagram(Solution, s,t))