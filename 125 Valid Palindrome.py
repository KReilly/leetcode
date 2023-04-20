class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(ch for ch in s if ch.isalnum())
        a = a.lower()
        b = a[::-1]
        print(a, b)
        if(a == b):
            return True
        else:
            return False


s = "A man, a plan, a canal: Panama"
s = "race a car"
#s = " "

print(Solution.isPalindrome(Solution, s))