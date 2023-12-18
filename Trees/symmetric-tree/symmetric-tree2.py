# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        
        if not root:
            return True
        
        return self.symmetry(root.left, root.right)
        
    def symmetry(self, left, right):
        
        if not left and not right:
            return True
        
        if not left or not right or left.val != right.val:
            return False
        
        return (self.symmetry(left.left, right.right) and
        self.symmetry(right.left, left.right))