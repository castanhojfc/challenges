"""
Problem:
Find all the paths in a binary tree.

Solution:
Traverse all the nodes, when a new node is found append it to the result.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/binary-tree-paths/
"""
from typing import List
from common import TreeNode, buildTree


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        if not root.left and not root.right:
            return [f"{root.val}"]

        res = []
        if root.left:
            for string in self.binaryTreePaths(root.left):
                res.append(f"{root.val}->{string}")

        if root.right:
            for string in self.binaryTreePaths(root.right):
                res.append(f"{root.val}->{string}")

        return res


if __name__ == '__main__':
    solution = Solution()

    # ["1->2->5", "1->3"]
    root = [1, 2, 3, None, 5]
    print(solution.binaryTreePaths(buildTree(root)))
