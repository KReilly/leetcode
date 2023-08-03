class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        max = a
        if(b>a):
            max = b
        count = 0
        for i in range(1, max+1):
            if (a%i == 0 and b%i == 0):
                count+=1
        return count

a = 12
b = 6

print(Solution.commonFactors(Solution, a, b))