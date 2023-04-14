from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in image:
            r.reverse()
            for i in range(len(r)):
                if(r[i] == 1):
                    r[i] = 0
                else:
                    r[i] = 1
        return image
    
image = [[1,1,0],[1,0,1],[0,0,0]]
image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

print(Solution.flipAndInvertImage(Solution, image))