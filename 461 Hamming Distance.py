class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xstr = format(x, '#033b')
        ystr = format(y, '#033b')
        
        count = sum(1 for a, b in zip(xstr, ystr) if a != b)

        return count



x = 680142203
y = 1111953568

#x = 3
#y = 1

print(Solution.hammingDistance(Solution, x, y))