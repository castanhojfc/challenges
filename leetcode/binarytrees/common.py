class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(array, root=None, i=0):
    n = len(array)

    if i < n:
        root = TreeNode(array[i])

        root.left = buildTree(array, root.left, 2 * i + 1)
        root.right = buildTree(array, root.right, 2 * i + 2)

    return root