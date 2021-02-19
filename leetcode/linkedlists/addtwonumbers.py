"""
Problem:
Calculate the sum of two numbers in reverse order.

Solution:
The trick is to keep track of the carry.
Traverse the two lists at the same time.
Keep summing all the numbers.
The current node will always be the last digit from the carry.
Computing the modulus by 10 gives us this number.
When the two lists have no more numbers we keep iterating
and getting more numbers from the carry. We check both lists
separately to deal with lists of different sizes.

Runtimes:
Time: O(max(M,N))
Space: O(max(M,N)) + 1 -> O(max(M,N))

https://medium.com/@rachit.slt/leetcode-add-two-numbers-486acc6aa8b8
"""
from commons import ListNode, printLinkedList


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        carry = 0
        n = res

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = divmod(carry, 10)

            n.next = ListNode(val)
            n = n.next

        return res.next


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    head = solution.addTwoNumbers(node1, node4)

    printLinkedList(head)
