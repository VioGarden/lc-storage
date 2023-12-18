# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs stack iterative solution

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right and val == targetSum:
                return True
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
        return False