# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        curr = root
        
        while curr:
            if q.val > curr.val and p.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
