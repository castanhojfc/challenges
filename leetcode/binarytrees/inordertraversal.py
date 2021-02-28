"""
Problem:
Traverse binary tree in order.

Solution:
Traverse all the nodes from the left.
Before switching to those in the right append them to the result.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
from typing import List
from common import TreeNode, buildTree


class Solution:
    def nodeTraverse(self, root: TreeNode, result):
        if root.left:
            self.nodeTraverse(root.left, result)

        if root.val:
            result.append(root.val)

        if root.right:
            self.nodeTraverse(root.right, result)

        return result

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []

        return self.nodeTraverse(root, result)


if __name__ == '__main__':
    solution = Solution()

    root = [1, None, 2, 3]
    print(solution.inorderTraversal(buildTree(root)))
