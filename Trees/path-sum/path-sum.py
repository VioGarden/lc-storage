# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution

class Solution:
    def hasPathSum(self, root, targetSum):
        result = []
        self.dfs(root, targetSum, result)
        return any(result)

    def dfs(self, root, target, result):
        if root:
            if not root.left and not root.right and root.val == target:
                result.append(True)
            if root.left:
                self.dfs(root.left, target-root.val, result)
            if root.right:
                self.dfs(root.right, target-root.val, result)
        