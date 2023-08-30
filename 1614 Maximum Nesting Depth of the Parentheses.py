class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        count = 0
        for c in s:
            if(c == "("):
                count+=1
                if(count>m):
                    m = count
            elif(c == ")"):
                count-=1


        return m
    




s = "(1+(2*3)+((8)/4))+1"
#s = "(1)+((2))+(((3)))"
print(Solution.maxDepth(Solution, s))