"""
Problem:
Check if the elements in a linked list form a palindrome.

Solution:
Traverse the linked list using two pointers.
The first pointer traverses two nodes at a time.
The loop ends when this pointer does not have a node and no next node.
The other pointer will always point to the middle value.
Reverse the second half of the linked list using the slow pointer.
The pointer that points to the previous value is used to perform the next check,
which is to go through the two parts separately and check if they have diferent
values.

Runtimes:
Time: O(n)
Space: O(1)

https://leetcode.com/problems/palindrome-linked-list/
"""
from commons import ListNode

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None

        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(solution.isPalindrome(node1))

