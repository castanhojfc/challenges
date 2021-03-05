"""
Problem:
Check if a binary search tree is valid.

Solution:
If a binary tree is balanced when traversing the tree one should get all the elements in order.
Just traverse the tree in order and put all the elements in an array.
Then go through each element and check if all the elements are ordered.

Runtimes:
Time: O(N)
Space: O(N)

https://leetcode.com/problems/validate-binary-search-tree/
"""
from typing import List
from common import TreeNode, buildTree


class Solution:
    def isValidBST(self, root):
        inorder = self.inorderTraversal(root)

        for i in range(1, len(inorder)):
            if inorder[i - 1] >= inorder[i]:
                return False

        return True

    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [
            root.val
        ] + self.inorderTraversal(root.right) if root else []


if __name__ == '__main__':
    solution = Solution()

    root = [2, 1, 3]
    print(solution.isValidBST(buildTree(root)))