class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        c1, c2 = 0,0
        for c in s1:
            if(c =="a" or c =="e" or c =="i" or c =="o" or c =="u"):
                c1+=1
        for c in s2:
            if(c =="a" or c =="e" or c =="i" or c =="o" or c =="u"):
                c2+=1
        return c1==c2

        

s = "book"

#s = "textbook"

print(Solution.halvesAreAlike(Solution, s))