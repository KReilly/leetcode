from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        print(s)
        for i in range(size//2):
            tmp = s[i]
            s[i] = s[size-i-1]
            s[size-i-1] = tmp
        print(s)


s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]

Solution.reverseString(Solution, s)