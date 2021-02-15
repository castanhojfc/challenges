"""
Problem:
Rotate linked list clockwise, kth times.

Solution:
First compute the length of the list and track the last node.
The next step is to figure the number of rotations.
If k is higher than the length, the real kth is given by
the modulus of the two.
The number of rotations is given by the difference between the length and k.
The next step is to find the node immediately before k, this is the kth node.
Then do the following:
Attach the head to the next node of the last node.
The first node(head) is now the next node of the kth node.
The next node of the kth node should now be detached.

Runtimes:
Time: O(N)
Space: O(1)

https://leetcode.com/problems/rotate-list/
"""

from commons import ListNode, printLinkedList


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        tmp = head
        len = 1

        while tmp.next:
            tmp = tmp.next
            len += 1

        if k > len:
            k %= len

        k = len - k

        if k == 0 or k == len:
            return head

        curr = head
        count = 1

        while count < k and curr:
            curr = curr.next
            count += 1

        if not curr:
            return head

        kthnode = curr
        tmp.next = head
        head = kthnode.next
        kthnode.next = None

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

    head = solution.rotateRight(node1, 2)
    printLinkedList(head)

    node1 = ListNode(0)
    node2 = ListNode(1)
    node3 = ListNode(2)

    node1.next = node2
    node2.next = node3

    head = solution.rotateRight(node1, 4)
    printLinkedList(head)