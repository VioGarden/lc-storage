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
        else:
            return self.inorderTraversal(root.left) + \
                [root.val] + self.inorderTraversal(root.right)
                

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return root
        answer = []
        def dfs(node):
            if node is not None:
                dfs(node.left)
                answer.append(node.val)
                dfs(node.right)
        dfs(root)
        return answer


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree_vals = []

        def inorder(tree):
            if tree:
                inorder(tree.left)
                tree_vals.append(tree.val)
                inorder(tree.right)
        
        inorder(root)
        return tree_vals


    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result = []
        self.inorder(root, result)
        return result


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
       
