"""
Problem:
Populate the next right pointers in each node.

Solution:
Traverse all the nodes.
Connect the left child to the right child.
For the right child find the next node of the parent.
Connect the right child to the left child of next node of parent.

Runtimes:
Time: O(n/2)
Space: O(1)

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""


class Node:
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return

        if root.left:
            root.left.next = root.right

        if root.next and root.right:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root


# TODO: Skipped the driver code here to save some time.
# I would have to implement another buildTree method to support the new type.
