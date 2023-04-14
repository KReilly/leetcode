class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        s = str(bin(n))
        print(s)
        s = s[2:]
        print(s)
        s = s[::-1]
        print(s)
        n = int(s, 2)
        
        return n
    

n = 0b00000010100101000001111010011100

#n = 0b11111111111111111111111111111101


print(Solution.reverseBits(Solution, n))