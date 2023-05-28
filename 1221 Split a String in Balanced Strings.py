class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sum = 0
        count = 0

        for c in s:
            if(c == "R"):
                sum+=1
            if(c=="L"):
                sum-=1
            if(sum == 0):
                count+=1
        
        return count



s = "RLRRLLRLRL"
#s = "RLRRRLLRLL"
#s = "LLLLRRRR"

print(Solution.balancedStringSplit(Solution, s))