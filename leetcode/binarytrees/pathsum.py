"""
Problem:
Check if there is a path where the sum of all nodes matches a number.

Solution:
Traverse all the nodes.
When traversing remove the current val from the target.
Once a leaf is reached the larget should be equal to the remaining.
Basically the remaining starts at the target and stops when it is equal to the last node value.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/path-sum/
"""
from common import TreeNode, buildTree


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return True if root.val == targetSum else False

        remaining = targetSum - root.val

        return self.hasPathSum(root.left, remaining) or self.hasPathSum(
            root.right, remaining)


if __name__ == '__main__':
    solution = Solution()

    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22

    print(solution.hasPathSum(buildTree(root), targetSum))