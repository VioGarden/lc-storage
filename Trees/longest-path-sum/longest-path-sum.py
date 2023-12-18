def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right and root.val == targetSum:
        return True
    targetSum -= root.val
    return hasPathSum(root.right, targetSum) or hasPathSum(root.left, targetSum)