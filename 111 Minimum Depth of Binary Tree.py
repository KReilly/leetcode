from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def helper(self, root, length):
    #     if not root:
    #         return length
    #     length = length+1
    #     return min(self.helper(self, root.left, length), self.helper(self, root.right, length) )

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # return self.helper(self, root, 0)
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(self, root.left), self.minDepth(self, root.right)) + 1
        else:
            return min(self.minDepth(self, root.left), self.minDepth(self, root.right)) + 1
        

def build(r, i=0):
    if(i >= len(r) or r[i] == None):
        return None
    a = TreeNode(r[i], None, None)
    a.left = build(r, i+1)
    a.right = build(r, i+2)
    return a

root = [3,9,20,None,None,15,7]
root = [2,None,3,None,4,None,5,None,6]
root = build(root)

print(Solution.minDepth(Solution, root))