from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root is None):
            return False
        if(root.left is None and root.right is None and targetSum == root.val):
            return True
        return self.hasPathSum(self, root.left, targetSum-root.val) or self.hasPathSum(self, root.right, targetSum-root.val) 

        



root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
# root = [1,2,3]
# targetSum = 5
# root = []
# targetSum = 0

def build(r, i=0):
    if(i >= len(r) or r[i] == None):
        return None
    a = TreeNode(r[i], None, None)
    a.left = build(r, i+1)
    a.right = build(r, i+2)
    return a

root = build(root)
print(Solution.hasPathSum(Solution, root, targetSum))