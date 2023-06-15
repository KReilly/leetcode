class Solution:
    def replaceDigits(self, s: str) -> str:
        # n = ""

        # for i in range(len(s)//2):
        #     n += s[i*2]
        #     if()
        #     a = chr(ord(s[i*2])+int(s[i*2+1]))
        #     n+=a


        # return n
        a = list(s)
        for i in range(1, len(a), 2):
            a[i] = chr(ord(a[i - 1]) + int(a[i]))
        return ''.join(a)


s = "a1c1e1"
print(Solution.replaceDigits(Solution, s))