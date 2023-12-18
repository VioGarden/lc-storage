from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs deque iterative solution

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        d = deque()
        d.append((root, root.val))
        while d:
            curr, val = d.popleft()
            if not curr.right and not curr.left and val == targetSum:
                return True
            if curr.right:
                d.append((curr.right, val + curr.right.val))
            if curr.left:
                d.append((curr.left, val + curr.left.val))
        return False