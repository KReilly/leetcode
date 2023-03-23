from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root, a):
        if(root is not None):
            a.append(root.val)
            Solution.helper(self, root.left, a)
            Solution.helper(self, root.right, a)


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        Solution.helper(self, root, a)
        return a

r = [1,None,2,3]
r = []
r = [1]

def build(r, i=0):
    if(i >= len(r) or r[i] == None):
        return None
    a = TreeNode(r[i], None, None)
    a.left = build(r, i+1)
    a.right = build(r, i+2)
    return a

root = build(r)

print(Solution.preorderTraversal(Solution, root))

