from typing import Optional
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(p, q, a):
        if(p!=None and q!= None):
            Solution.helper(p.left, q.left, a)
            if(p.val != q.val):
                a.append(False)
            Solution.helper(p.right, q.right, a)
        elif(p == None and q != None):
            a.append(False)
        elif(p != None and q == None):
            a.append(False)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = []
        Solution.helper(p,q,a)
        for n in range(0,len(a)):
            if(n == False):
                return False
        return True
        # p1 = []
        # Solution.helper(p, p1)
        # q1 = []
        # Solution.helper(q, q1)

        # isSame = True
        # if(len(p1) == len(q1)):
        #     for n in range(0, len(p1)):
        #         if(p1[n] != q1[n]):
        #             isSame = isSame and False
        #     return isSame
        # else:
        #     return False



def build(i, r):
    if(i >= len(r) or r[i] == None):
        return None
    a = TreeNode(r[i], None, None)
    a.left = build(i+1, r)
    a.right = build(i+2, r)
    return a

p1 = [1,2,3]
q1 = [1,2,3]
# p1 = [1,2]
# q1 = [1,None,2]
# p1 = [1,2,1]
# q1 = [1,1,2]

p = build(0, p1)
q = build(0, q1)

print(Solution.isSameTree(Solution, p,q))
