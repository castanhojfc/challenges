"""
Problem:
Determine the minimum depth of a binary tree.

Solution:
Traverse all the nodes and add one per each node.
Select the minimum between the results.
If one node is not present, just use the other half.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
from common import TreeNode, buildTree


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)

        return (1 + min(self.minDepth(root.left), self.minDepth(root.right)))


if __name__ == '__main__':
    solution = Solution()

    root = buildTree([3, 9, 20, None, None, 15, 7])
    print(solution.minDepth(root))