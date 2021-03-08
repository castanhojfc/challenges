"""
Problem:
Find the maximum path sum in a binary tree.

Solution:
Just run DFS through all the nodes.
The answer starts at the mininum number possible.
The current answer is always be given by the max path sum of the left
plus the max path sum of the right and the current root value.
Always determine the maximum value between the current answer and the previous.
To determine the maximum path value of a path that is returned by DFS:
Compute the maximum value between the maximum path between the left and the right.
Finally add the root and return the maximum between 0 and the two branches.
We need to do the step above because we may have negative numbers and we may be
returning a negative number at the end and we do not want that.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""
from common import TreeNode, buildTree


class Solution:
    def dfs(self, root: TreeNode):
        if not root:
            return 0

        x = self.dfs(root.left)
        y = self.dfs(root.right)

        sum = x + y

        if root.val:
            sum += root.val

        self.answer = max(self.answer, sum)

        sum = max(x, y)

        if root.val:
            sum += root.val

        return max(0, sum)

    def maxPathSum(self, root: TreeNode) -> int:
        self.answer = float('-inf')
        self.dfs(root)

        return self.answer


if __name__ == '__main__':
    solution = Solution()

    root = [1, 2, 3]
    print(solution.maxPathSum(buildTree(root)))

    root = [-10, 9, 20, None, None, 15, 7]
    print(solution.maxPathSum(buildTree(root)))