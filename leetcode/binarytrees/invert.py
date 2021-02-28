"""
Problem:
Invert a binary tree.

Solution:
Traverse each node and swap the left node with the one in the right.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/invert-binary-tree/
"""
from common import TreeNode, buildTree, printTree


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.left = right
        root.right = left

        return root

    def invertTreeAlternative(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        if root:
            tmp = root.right
            root.right = root.left
            root.left = tmp

        if root.left:
            self.invertTree(root.left)

        if root.right:
            self.invertTree(root.right)

        return root


if __name__ == '__main__':
    solution = Solution()

    root = buildTree([4, 2, 7, 1, 3, 6, 9])
    printTree(solution.invertTree(root))