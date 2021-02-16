"""
Problem:
Swap node pairs.

Solution:
Add a dummy node at the start to ease processing.
At the end return its next node.
Set the previous node to dummy and the current to head.
Iterate through the list. Perform swaps using a temp node.
The swap is performed by saving the next value to the pair.
Set the next node to the temp node.

Runtimes:
Time: O(N)
Space: O(1)

https://leetcode.com/problems/swap-nodes-in-pairs/
"""

from commons import ListNode, printLinkedList


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prehead = ListNode(0)
        prehead.next = head
        prev = prehead
        curr = head

        while curr and curr.next:
            temp = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = temp

            prev = curr
            curr = curr.next

        return prehead.next


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    head = solution.swapPairs(node1)
    printLinkedList(head)
