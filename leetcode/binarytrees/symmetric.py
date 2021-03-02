"""
Problem:
Check if a binary tree is symmetric.

Solution:


Runtimes:
https://leetcode.com/problems/symmetric-tree/
"""
from common import TreeNode, buildTree


class Solution:
    def isSymmetric(self, root):
        return not root or self.traverse(root.left, root.right)

    def traverse(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return left.val == right.val and self.traverse(
            left.right, right.left) and self.traverse(right.right, left.left)


if __name__ == '__main__':
    solution = Solution()

    root = [1, 2, 2, 3, 4, 4, 3]
    print(solution.isSymmetric(buildTree(root)))

    root = [1, 2, 2, None, 3, None, 3]
    print(solution.isSymmetric(buildTree(root)))

    root = [1, 2, 2, None, 3, None, 3]
    print(solution.isSymmetric(buildTree(root)))
