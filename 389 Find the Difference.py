class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 =''.join(sorted(s))
        t1 =''.join(sorted(t))

        i=0
        while(i<len(s1) and i<len(t1)):
            if(s1[i] != t1[i]):
                if(len(s1)>len(t1)):
                    return s1[i]
                else:
                    return t1[i]
            i+=1
        
        if(len(s1)>len(t1)):
            return s1[i]
        else:
            return t1[i]


s = "abcd"
t = "abcde"

# s = ""
# t = "y"

print(Solution.findTheDifference(Solution, s, t))