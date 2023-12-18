from collections import defaultdict

def maxLevelSum(root):

    levels = defaultdict(int)
    def helper(root, depth):
        if root:
            levels[depth] += root.val
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
    helper(root, 1)
    return max(levels, key=levels.get)