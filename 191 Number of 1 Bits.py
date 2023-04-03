class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


n= 0o00000000000000000000000000001011
n = 0o00000000000000000000000010000000
n = 0o11111111111111111111111111111101

print(Solution.hammingWeight(Solution, n))
