"""
Problem:
Delete a node by given node.
No access to the head is given and this node is never the tail.

Solution:
Just copy the information of the next node to the node given.

Runtimes:
Time: O(1)
Space: O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    solution.deleteNode(node3)
