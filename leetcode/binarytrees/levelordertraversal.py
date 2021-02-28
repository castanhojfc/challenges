"""
Problem:
Return the level order traversal of a binary tree.

Solution:
Put all the nodes in a level in a list.
Find the nodes in the next level and append them to the list above.
Keep repeating untill all the nodes are traversed.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from typing import List
from common import TreeNode, buildTree


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        res, st = [], [root]

        while st:
            res.append([node.val for node in st])
            st = [
                child for node in st for child in (node.left, node.right)
                if child
            ]

        return res

    def levelOrderAlternative(self, root: TreeNode) -> List[List[int]]:
        result = []

        if root:
            result.append([root.val])

            currentLevelValues = []
            currentLevelNodes = []
            if root.left:
                currentLevelValues.append(root.left.val)
                currentLevelNodes.append(root.left)
            if root.right:
                currentLevelValues.append(root.right.val)
                currentLevelNodes.append(root.right)
            if currentLevelNodes:
                result.append(currentLevelValues)

                lastLevelNodes = currentLevelNodes
                nextLevelNodes = []
                nextLevelValues = []

                while lastLevelNodes:
                    for node in lastLevelNodes:
                        if node.left:
                            nextLevelNodes.append(node.left)
                            nextLevelValues.append(node.left.val)

                        if node.right:
                            nextLevelNodes.append(node.right)
                            nextLevelValues.append(node.right.val)

                    if nextLevelNodes:
                        result.append(nextLevelValues)

                    lastLevelNodes = nextLevelNodes
                    nextLevelNodes = []
                    nextLevelValues = []

        return result


if __name__ == '__main__':
    solution = Solution()

    root = buildTree([3, 9, 20, None, None, 15, 7])
    print(solution.levelOrder(root))

    root = buildTree([1])
    print(solution.levelOrder(root))

    root = buildTree([])
    print(solution.levelOrder(root))