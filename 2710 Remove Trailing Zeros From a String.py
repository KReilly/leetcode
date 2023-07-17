class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n2 = num[::-1]
        n = int(n2)
        n = str(n)
        n = n[::-1]
        return n




num = "51230100"

print(Solution.removeTrailingZeros(Solution, num))