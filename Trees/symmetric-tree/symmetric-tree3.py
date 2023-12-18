from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        queue = deque()
        queue.append([root.left, root.right])
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                queue.appendleft([left.left, right.right])
                queue.appendleft([left.right, right.left])
            else:
                return False
        return True