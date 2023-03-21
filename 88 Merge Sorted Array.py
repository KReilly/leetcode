from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0

        for i in range(0,n):
            nums1[m+i] = nums2[i]
        nums1.sort()

        # while(p1 < m+n or p2 < n):
        #     if(nums1[p1]>=nums2[p2]):
        #         temp = nums1[p1]
        #         nums1[p1] = nums2[p2]
        #         nums1[p2] = temp
        #         p1+=1
        #     else:
        #         p2+=1


        #print(nums1)


nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3

Solution.merge(Solution, nums1, m, nums2, n)