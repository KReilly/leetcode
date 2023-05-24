from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        cells = [[0 for i in range(n)] for j in range(m)]
        
        for [x,y] in indices:
            for i in range(m):
                for j in range(n):
                    if(x == i):
                        cells[i][j] += 1
                    if(y == j):
                        cells[i][j] += 1
            # print(cells)

        count = 0
        for i in range(m):
                for j in range(n):
                    if(cells[i][j]%2 == 1):
                        count +=1
            
        # print(cells)

        return count



m = 2
n = 3
indices = [[0,1],[1,1]]

m = 2
n = 2 
indices = [[1,1],[0,0]]

print(Solution.oddCells(Solution, m, n, indices))