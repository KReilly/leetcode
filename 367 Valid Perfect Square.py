class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        print(num//2)
        for n in range(1, (num)//2+2):
            if(n*n == num):
                return True
            if(n*n>num):
                return False
        return False




num = 1
#num = 14

print(Solution.isPerfectSquare(Solution, num))