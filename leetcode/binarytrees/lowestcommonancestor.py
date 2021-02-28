"""
Problem:
Find the lower common ancestor of a binary search tree.

Solution:
Traverse the tree. Track the current node.
If both p and q are lower than the current value, pick the left node.
If both p and q are higher, pick the right node.
This can be done recursively.

Runtimes:
Time: O(n)
Space: O(1)

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
from common import TreeNode, buildTree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


if __name__ == '__main__':
    solution = Solution()

    print(
        solution.lowestCommonAncestor(
            buildTree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), TreeNode(2),
            TreeNode(8)).val)
