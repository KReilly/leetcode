from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        for i in range(0, len(digits)):
            digits[i]+=carry 
            carry = int(digits[i]/10) 
            digits[i] = digits[i] %10
        if(carry == 1):
            digits.append(carry)
        digits.reverse()
        return digits
    

digits = [1,2,3]
digits = [9]

print(Solution.plusOne(Solution, digits))