"""
Problem:
Merge two sorted linked lists.

Solution:
Create an extra linked list to store the result.
Keep iterating both lists.
Keep putting the lower value between l1 and l2 to the resulting list.
At the end, check the list that still contains values.
Attach this list to the result.

Runtimes:
Time: O(min(M,N))
Space: O(1)

https://leetcode.com/problems/merge-two-sorted-lists/
"""
from commons import ListNode, printLinkedList


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        iter = res

        while l1 and l2:
            if l1.val < l2.val:
                iter.next = l1
                l1 = l1.next
            else:
                iter.next = l2
                l2 = l2.next

            iter = iter.next

        if l1:
            iter.next = l1
        else:
            iter.next = l2

        return res.next


if __name__ == '__main__':
    solution = Solution()

    l1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)

    l1.next = node2
    node2.next = node3

    l2 = ListNode(1)
    node4 = ListNode(3)
    node5 = ListNode(4)

    l2.next = node4
    node4.next = node5

    head = solution.mergeTwoLists(l1, l2)
    printLinkedList(head)
