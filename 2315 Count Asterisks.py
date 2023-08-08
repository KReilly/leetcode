class Solution:
    def countAsterisks(self, s: str) -> int:
        spls = s.split("|")
        count = 0
        for i in range(len(spls)):
            if(i%2==0):
                count += spls[i].count("*")
        return count




s = "l|*e*et|c**o|*de|"
#s = "iamprogrammer"
#s = "yo|uar|e**|b|e***au|tifu|l"

print(Solution.countAsterisks(Solution, s))