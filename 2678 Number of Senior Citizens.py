from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sen = 0

        for d in details:
            age = d[11:13]
            age = int(age)
            if(age>60):
                sen+=1




        return sen
    
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(Solution.countSeniors(Solution, details))