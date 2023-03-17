class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ""
        x= int(a,2)
        y = int(b,2)
        sum = x+y
        sum = str(bin(sum))[2:]
        return sum



a = "11"
b = "1"
# a = "1010"
# b = "1011"

print(Solution.addBinary(Solution, a,b))
