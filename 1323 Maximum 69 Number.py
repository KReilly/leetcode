class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        r = ""
        hasChanged = False
        for c in s:
            if( hasChanged == False and c == "6"):
                r += "9"
                hasChanged = True
            else:
                r += c
        return int(r)


num = 9669
print(Solution.maximum69Number(Solution, num))