class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
    


s = "Hello World"
s = "   fly me   to   the moon  "

print(Solution.lengthOfLastWord(Solution, s))

