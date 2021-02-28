"""
Problem:
Traverse binary tree in pre-order.

Solution:
Traverse all the nodes. But before doing so add the current node to the result.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from typing import List
from common import TreeNode, buildTree


class Solution:
    def nodeTraverse(self, root: TreeNode, result):
        if root.val:
            result.append(root.val)

        if root.left:
            self.nodeTraverse(root.left, result)

        if root.right:
            self.nodeTraverse(root.right, result)

        return result

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []

        return self.nodeTraverse(root, result)


if __name__ == '__main__':
    solution = Solution()

    root = [1, None, 2, 3]
    print(solution.preorderTraversal(buildTree(root)))
