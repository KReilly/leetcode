from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root, length):
        if not root:
            return length
        length = length+1
        return max(self.helper(self, root.left, length), self.helper(self, root.right, length) )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(self, root, 0)
    

def build(r, i=0):
    if(i >= len(r) or r[i] == None):
        return None
    a = TreeNode(r[i], None, None)
    a.left = build(r, i+1)
    a.right = build(r, i+2)
    return a

root = [3,9,20,None,None,15,7]
#root = [1,None,2]
root = build(root)
print(Solution.maxDepth(Solution, root))
