class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1

        while(n > 1):
            r = n%10
            n = n//10
            sum +=r
            product *=r
        


        return product - sum


n = 234
n = 4421

print(Solution.subtractProductAndSum(Solution, n))