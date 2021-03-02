"""
Problem:
Determine if a binary tree is balanced.

Solution:
Use post order traversal check height and balance per call and propogate it upwards.
In other languages, we can return an error code in height. Complexity O(N) and space is O(h).

Runtimes:
Time: O(n)
Space: O(height)

https://leetcode.com/problems/balanced-binary-tree/description/
"""
from common import TreeNode, buildTree


class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0, True

        height_left, left_balanced = self.maxDepth(root.left)
        height_right, right_balanced = self.maxDepth(root.right)

        if left_balanced and right_balanced and abs(height_left -
                                                    height_right) <= 1:
            return max(height_left, height_right) + 1, True
        else:
            return -1, False

    def isBalanced(self, root):
        _, balanced = self.maxDepth(root)

        return balanced


if __name__ == '__main__':
    solution = Solution()

    root = [3, 9, 20, None, None, 15, 7]
    print(solution.isBalanced(buildTree(root)))

    root = [1, 2, 2, 3, 3, None, None, 4, 4]
    print(solution.isBalanced(buildTree(root)))

    root = []
    print(solution.isBalanced(buildTree(root)))