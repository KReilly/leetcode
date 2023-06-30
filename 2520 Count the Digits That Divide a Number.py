class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        count = 0
        while(n > 0):
            d = n%10
            print(d)
            if(num%d == 0):
                count +=1
            n = n//10
        return count

num = 7
print(Solution.countDigits(Solution, num))