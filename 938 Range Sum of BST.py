from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # sum = 0
        # def helper(self, root):
        #     nonlocal sum
        #     if(root!=None):
        #         if(root.val >= low or root.val <=high):
        #             sum += root.val
        #         helper(self, root.left)
        #         helper(self, root.right)
        # helper(self, root)
        # return sum

        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans


root = [10,5,15,3,7,None,18]
low = 7
high = 15

root = [10,5,15,3,7,13,18,1,None,6]
low = 6 
high = 10

def build(i, r):
    if(i >= len(r) or r[i] == None):
        return None
    a = TreeNode(r[i], None, None)
    a.left = build(i+1, r)  
    a.right = build(i+2, r)
    return a

p = build(0, root)

print(Solution.rangeSumBST(Solution, p, low, high))