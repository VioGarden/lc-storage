# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root==None:
            return []
        preorder = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

    def preorderTraversal(self, root): 
        return [root.val] + \
        self.preorderTraversal(root.left) + \
        self.preorderTraversal(root.right) if root else []

    def preorderTraversal(self, root):
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res
    def helper(self, node, res):
        if not node:
            return
        res.append(node.val)
        self.helper(node.left, res)
        self.helper(node.right, res)
        return