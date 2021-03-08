"""
Problem:
Find the visible values from the right in a binary tree.

Solution:
Use BFS. The trick is to alway check the last value in the queue and append it to the result.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/binary-tree-right-side-view/
"""
from typing import Deque, List
from common import TreeNode, buildTree


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        visible = []

        if not root:
            return visible

        queue = Deque()
        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                current = queue.popleft()

                if i == (size - 1):
                    visible.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

        return visible


if __name__ == '__main__':
    solution = Solution()

    root = [1, 2, 3, None, 5, None, 4]
    print(solution.rightSideView(buildTree(root)))

    root = [1, None, 3]
    print(solution.rightSideView(buildTree(root)))

    root = []
    print(solution.rightSideView(buildTree(root)))

    root = [1, 2, 3, 4]
    print(solution.rightSideView(buildTree(root)))