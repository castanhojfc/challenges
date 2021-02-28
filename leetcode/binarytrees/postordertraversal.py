"""
Problem:
Traverse binary tree in post-order.

Solution:
Traverse all the nodes.
After traversing the last node, begin to add it to the result.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/binary-tree-postorder-traversal//
"""
from typing import List
from common import TreeNode, buildTree


class Solution:
    def nodeTraverse(self, root: TreeNode, result):
        if root.left:
            self.nodeTraverse(root.left, result)

        if root.right:
            self.nodeTraverse(root.right, result)

        if root.val:
            result.append(root.val)

        return result

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []

        return self.nodeTraverse(root, result)


if __name__ == '__main__':
    solution = Solution()

    root = [1, None, 2, 3]
    print(solution.postorderTraversal(buildTree(root)))
