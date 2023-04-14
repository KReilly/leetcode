from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for o in operations:
            if(o == "C"):
                record.pop()
            elif(o == "+"):
                record.append(record[-1]+record[-2])
            elif(o == "D"):
                record.append(record[-1]*2)
            else:
                record.append(int(o))
        
        sum = 0
        for r in record:
            sum += r

        return sum
    

ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
ops = ["1","C"]


print(Solution.calPoints(Solution, ops))