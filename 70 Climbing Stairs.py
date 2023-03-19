class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0 for x in range(46)]
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2
        for x in range(2, len(steps)):
            steps[x] = steps[x-1] + steps[x-2] 
        return steps[n+1]

n = 3
print(Solution.climbStairs(Solution, n))