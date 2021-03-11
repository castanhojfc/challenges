"""
Problem:
Flatten binary tree to linked list.

Solution:
Use pre-order traversal and a stack.
The stack should always contain the current nodes/sub.trees to the left and the right and starts at root.
We use a dummny node to start to organize nodes correctly from the start.
The previous sub-tree is selected and we move it to the right while never having a left node.
The last step is to choose the next node which will be the node to the right.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""
from common import TreeNode, buildTree, printTree


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return None

        dummy = TreeNode(0)
        stack = [root]

        while stack:
            previous = stack.pop()

            if previous.right:
                stack.append(previous.right)

            if previous.left:
                stack.append(previous.left)

            dummy.right = previous
            previous.left = None
            dummy = dummy.right


if __name__ == '__main__':
    solution = Solution()

    root = [1, 2, 5, 3, 4, None, 6]
    solution.flatten(buildTree(root))
    printTree(buildTree(root))