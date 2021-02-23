class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TODO: Check this method, it may not be producting the correct results.
def buildTree(array, root=None, i=0):
    n = len(array)

    if i < n:
        root = TreeNode(array[i])

        root.left = buildTree(array, root.left, 2 * i + 1)
        root.right = buildTree(array, root.right, 2 * i + 2)

    return root