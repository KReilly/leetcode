class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        flipX = strX[::-1]
        return ( strX == flipX)


x=313
s = Solution.isPalindrome(Solution, x) 
print(x, s)