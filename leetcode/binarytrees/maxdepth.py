"""
Problem:
Determine the max depth of a binary tree.

Solution:
For each node traversed increase the result in one.
Perform the search for each node recursively and select the max value.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
from common import TreeNode, buildTree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return (max(l, r) + 1)


if __name__ == '__main__':
    solution = Solution()

    root = buildTree([3, 9, 20, None, None, 15, 7])
    print(solution.maxDepth(root))