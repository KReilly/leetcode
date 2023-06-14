from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for o in operations:
            if(o == "X++" or o == "++X"):
                x+=1
            elif(o == "X--" or o == "--X"):
                x-=1

        return x
    


operations = ["X++","++X","--X","X--"]

print(Solution.finalValueAfterOperations(Solution, operations))