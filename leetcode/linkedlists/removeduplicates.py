"""
Problem:

Solution:

Runtimes:

https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
from commons import ListNode, printLinkedList

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        p = head

        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next

        return head

if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    head = solution.deleteDuplicates(node1)

    printLinkedList(head)