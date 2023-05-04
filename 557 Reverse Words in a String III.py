class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        print(words)
        r = ""
        for w in words:
            r+=w[::-1]+" "
        return r[:-1]


s = "Let's take LeetCode contest"
s = "God Ding"

print(Solution.reverseWords(Solution, s))