from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:        
        max = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            temp = min(height[r], height[l])*(r-l)
            if(temp > max):
                max = temp
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return max
        # max = 0
        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         temp = min(height[i], height[j])*(abs(i-j))
        #         if(temp > max):
        #             # print(height[i], height[j])
        #             max = temp

        # return max


height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
print(Solution.maxArea(Solution, height))