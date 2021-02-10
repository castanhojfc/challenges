"""
Problem:
Reverse a linked list.

Solution:
Keep track of three things:

1) the previous node, starts at None
2) current node, starts at the head
3) the next node

Do a loop starting at the head:
Compute the next node and store it in a variable.
The next value of the current node will be the previous value.
After this the update the previous value with the current node.
Update the current node with the next node.
Stop when there's no current node.

TODO: There is a recursive solution for this problem.
The space complexity is O(N) though.
Might be worth to study it later to learn more about recursion.

Runtimes:
Time: O(N)
Space: O(1)

https://leetcode.com/problems/reverse-linked-list/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = None
        curr = head

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return prev


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution.reverseList(node1)
