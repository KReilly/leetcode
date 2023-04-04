class Solution:
    def addDigits(self, num: int) -> int:
        solution = 0
        while(num > 0):
            solution += num%10
            num = num // 10
            if num == 0 and solution >9:
                num = solution
                solution = 0

        return solution




num = 38
#num = 0

print(Solution.addDigits(Solution, num))