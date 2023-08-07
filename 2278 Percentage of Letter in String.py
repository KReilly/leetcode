class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return (int)(s.count(letter) / len(s) *100)


s = "foobar"
letter = "o"

print(Solution.percentageLetter(Solution, s, letter))