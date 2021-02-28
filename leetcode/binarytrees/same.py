"""
Problem:
Check if two binary trees are the same.

Solution:
Traverse both trees at the same time and compare nodes.
If one of them does not have a value or if both values are different they are not the same.

Runtimes:
Time: O(n)
Space: O(log(n)) (to keep the recursion stack)

https://leetcode.com/problems/same-tree
"""
from common import TreeNode, buildTree, printTree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) and self.isSameTree(
            p.left, q.left)


if __name__ == '__main__':
    solution = Solution()

    p = [1, 2, 3]
    q = [1, 2, 3]

    print(solution.isSameTree(buildTree(p), buildTree(q)))