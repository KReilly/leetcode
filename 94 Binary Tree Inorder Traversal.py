from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(root, a):
        if(root!=None):
            Solution.helper(root.left, a)
            a.append(root.val)
            Solution.helper(root.right, a)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        Solution.helper(root, a)
        return a
    

            




r = [1,None,2,3]

r = []
r = [1]

def build(i, r):
    if(i >= len(r) or r[i] == None):
        return None
    a = TreeNode(r[i], None, None)
    a.left = build(i+1, r)
    a.right = build(i+2, r)
    return a

root = build(0, r)
    
print(Solution.inorderTraversal(Solution, root))