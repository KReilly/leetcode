class Solution:
    def replaceDigits(self, s: str) -> str:
        n = ""

        for i in range(len(s)//2):
            n += s[i*2]
            a = chr(ord(s[i*2])+int(s[i*2+1]))
            print(a)
            n+=a


        return n


s = "a1c1e1"
print(Solution.replaceDigits(Solution, s))