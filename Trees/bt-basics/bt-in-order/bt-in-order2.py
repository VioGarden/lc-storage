# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, roo):
        stack = []
        final = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                final.append(curr.val)
                root = curr.right
        
        return final
            

            
        