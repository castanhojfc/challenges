"""
Problem:
Partition list in a way that every value lower than k appears to the left.
Every value bigger should be in the right. The original positions should be maintained.

Solution:
Keep two linked lists.
One that keeps the values lower than k.
Another that keeps the values higher than k.
Clear the next node of the second list.
Attach the first list with the second.
One trick here is to create a dummy node for both.
When attaching and returning point to the next node.
Always keep track of the last node inserted for both listings.

Runtimes:
Time: O(N)
Space: O(1)

https://leetcode.com/problems/partition-list/
"""

from commons import ListNode, printLinkedList


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    head = solution.partition(node1, 3)
    printLinkedList(head)
