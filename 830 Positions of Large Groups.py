from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        begin, end = 0,0
        groups = []

        while(begin < len(s)):
            c = s[begin]
            while(end< len(s) and c == s[end]):
                end += 1
            if(end-begin>=3):
                groups.append([begin, end-1])
            begin = end
            #end = end
        return groups

s = "abbxxxxzzy"
#s = "abc"
#s = "abcdddeeeeaabbbcd"

print(Solution.largeGroupPositions(Solution, s))