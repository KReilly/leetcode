from typing import List

# class Solution:
#     def search(self, A: List[int], target: int) -> int:
#         n = len(A)
#         left, right = 0, n - 1
#         if n == 0: return -1
        
#         while left <= right:
#             mid = left + (right - left) // 2
#             if A[mid] == target: return mid
            
#             # inflection point to the right. Left is strictly increasing
#             if A[mid] >= A[left]:
#                 if A[left] <= target < A[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
                    
#             # inflection point to the left of me. Right is strictly increasing
#             else:
#                 if A[mid] < target <= A[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
            
#         return -1

class Solution:
    def search(self, A: List[int], target: int) -> int:
        def shift(i, p):
            if i>p :
                return i-p
            else :
                return p-i-1
        
        p = 0
        for i in range(len(A)):
            if(A[i] < A[p]):
                p = i
        

        low = 0
        high = len(A)
        while(high-low >1):
            mid = (high-low)//2 + low
            if(A[shift(mid, p)] == target):
                return shift(mid, p)
            elif(A[shift(mid, p)] > target):
                high = mid
            elif(A[shift(mid, p)] < target):
                low = mid 
        mid = (high-low)//2 + low
        print(mid)
        print(A[shift(mid, p)])
        if(A[shift(mid, p)] == target):
            return shift(mid, p)
        else:
            return -1
   

nums = [4,5,6,7,0,1,2]
target = 0
nums = [4,5,6,7,0,1,2]
target = 3
nums = [1]
target = 0
# nums = [3,5,1]
# target = 3


print(Solution.search(Solution, nums, target))