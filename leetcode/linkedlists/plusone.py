"""
Problem:
Given a non-negative number represented as a singly linked list of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.

Solution:
Reverse the linked list and traverse it.
If the current number is lower than 9, just add 1 and stop.
If not, set it to 0, if there is no next node create a new node with 1 and stop.
Reverse the list at the end again.

Runtimes:
Time: O(n)
Space: O(1)

https://leetcode.com/problems/plus-one-linked-list/
(this is only available with a subscription)
"""
from commons import ListNode, printLinkedList


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
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

    def plusOne(self, head: ListNode) -> ListNode:
        p = self.reverse(head)

        while p:
            if p.val + 1 <= 9:
                p.val += 1
                break
            else:
                p.val = 0

                if not p.next:
                    p.next = ListNode(1)
                    break

                p = p.next

        return self.reverse(p)


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    head = solution.plusOne(node1)

    printLinkedList(head)