from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng = []
        for n in nums1:
            found = False
            ngl = -1
            for i in range(len(nums2)):
                if(found and nums2[i] > n):
                    found = False
                    ngl = nums2[i]
                elif(found == False and nums2[i] == n):
                    found = True
            ng.append(ngl)
        return ng



nums1 = [4,1,2]
nums2 = [1,3,4,2]

# nums1 = [2,4]
# nums2 = [1,2,3,4]

print(Solution.nextGreaterElement(Solution, nums1, nums2))