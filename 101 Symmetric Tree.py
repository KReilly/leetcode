from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, p, q) -> bool:
        if(p is None and q is None):
             return True
        if p is None or q is None:
             return False
        if p.val == q.val:
             a = self.helper(self, p.left, q.right)
             b = self.helper(self, p.right, q.left)
             return a and b
        else:
             return False
        

        # if(p!=None and q!= None):
        #     if(p.val == q.val):
        #         return self.helper(self, p.left, q.right) and self.helper(self, p.right, q.left)
        # elif(p==None and q== None):
        #     return True
        # elif(p == None and q != None):
        #     return False
        # elif(p != None and q == None):
        #     return False
   
#    if left is None and right is None:
#       return True
#     if left is None or right is None:
#       return False

#     if left.val == right.val:
#       outPair = self.isMirror(left.left, right.right)
#       inPiar = self.isMirror(left.right, right.left)
#       return outPair and inPiar
#     else:
#       return False
    # def isMirror(self, left, right):
    #     if left is None and right is None:
    #         return True
    #     if left is None or right is None:
    #         return False

    #     if left.val == right.val:
    #         outPair = self.isMirror(self, left.left, right.right)
    #         inPiar = self.isMirror(self, left.right, right.left)
    #         return outPair and inPiar
    #     else:
    #         return False
    
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if(root is None):
    #         return True
    #     return Solution.isMirror(self, root.left, root.right)


    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)


def build(r, i=0):
    if(i >= len(r) or r[i] == None):
        return None
    a = TreeNode(r[i], None, None)
    a.left = build(r, i+1)
    a.right = build(r, i+2)
    return a

root = [1,2,2,3,4,4,3]
#root = [1,2,2,None,3,None,3]
root = build(root)
print(Solution.isSymmetric(Solution, root))