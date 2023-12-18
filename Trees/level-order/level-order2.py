# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        final, level = [], [root]
        while level:
            final.append([node.val for node in level])
            temp = []
            for i in level:
                temp.extend([i.left, i.right])
            level = [j for j in temp if j]
        return final
        