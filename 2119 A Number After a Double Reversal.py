class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num2 = str(num)
        num2 = num2[::-1]
        num2 = int(num2)

        num2 = str(num2)
        num2 = num2[::-1]
        num2 = int(num2)
        
        print(num, num2)
        return num == num2


num = 1800
#num = 526
#num = 0
print(Solution.isSameAfterReversals(Solution, num))