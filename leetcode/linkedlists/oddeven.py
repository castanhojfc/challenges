"""
Problem:
Given a linked list add the odd positioned nodes first and then the even positioned ones.

Solution:
Loop through the elements and stop when there is no more even values.
The next odd value will be the one next to the next even value.
The next even value will be the one next to the next odd value.
Update the odd and even pointers in each iteration.
The place where one should connect both parts should be saved before the loop,
it basically always points to the first even value. At the end connect the last
odd value to this node.

Runtimes:
Time: O(n)
Space: O(1)

https://leetcode.com/problems/odd-even-linked-list/
"""
from commons import ListNode, printLinkedList


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head


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

    head = solution.oddEvenList(node1)

    printLinkedList(head)