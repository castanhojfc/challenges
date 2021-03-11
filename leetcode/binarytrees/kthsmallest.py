"""
Problem:
Find the kth smallest

Solution:
Use a stack and traverse the tree and put all the nodes to the left in it.
Pop from the stack, and we have the last element.
We will now iterate from k to 0.
When k is 0 we are at the correct node and we just return its val.
Otherwise, we keep traversing the remaining nodes by selecting those from the right.

Runtimes:
Time: O(H)
Space: O(k + H) unbalanced trees, for balanced it is O(logN + k)

https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

from common import TreeNode, buildTree


class Solution:
    def inOrder(self, root):
        if not root:
            return []

        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def kthSmallestRecursive(self, root: TreeNode, k: int) -> int:
        return self.inOrder(root)[k - 1]

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1

            if not k:
                return root.val

            root = root.right


if __name__ == '__main__':
    solution = Solution()

    root = [5, 3, 6, 2, 4, None, None, 1]
    k = 3
    print(solution.kthSmallest(buildTree(root), k))