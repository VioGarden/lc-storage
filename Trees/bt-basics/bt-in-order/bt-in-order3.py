# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        def io(node):
            if node is None:
                return
            io(node.left)
            output.append(node.val)
            io(node.right)
        output = []
        io(root)
        return output

    