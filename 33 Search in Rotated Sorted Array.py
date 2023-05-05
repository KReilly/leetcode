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
        return -1
    

nums = [4,5,6,7,0,1,2]
target = 0
# nums = [4,5,6,7,0,1,2]
# target = 3
# nums = [1]
# target = 0

print(Solution.search(Solution, nums, target))