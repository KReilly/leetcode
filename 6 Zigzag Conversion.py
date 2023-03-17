class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        
        splits = []
        n = len(s)
        chars_per_section = 2*(numRows -1)

        for r in range(0,numRows):
            index = r
            while index < n:
                splits.append(s[index])
                if r != 0 and r != numRows - 1:
                    chars_in_between = chars_per_section - 2 * r
                    second_index = index + chars_in_between
                    
                    if second_index < n:
                        splits.append(s[second_index])
                index += chars_per_section
                
        return "".join(splits)

s = "PAYPALISHIRING"
numRows = 3

#numRows = 4
print(Solution.convert(Solution, s, numRows))
