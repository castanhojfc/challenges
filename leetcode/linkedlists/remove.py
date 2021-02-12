"""
Problem:
Remove all the elements from a linked list with a give value.

Solution:
Create a new node with val different than the target.
Put this node right at the start and save its position.
Traverse the linked list when val is found, connect the
node to the node next to the next one.
If not, keep making the current node the next one.
The solution will be given by the next node to the position saved
right at the start.

Runtimes:
Time: O(n)
Space: O(1)

https://leetcode.com/problems/remove-linked-list-elements/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def print(self, node) -> None:
        temp = node

        while (temp):
            print(temp.val, end="->")
            temp = temp.next

        print()

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(val - 1)
        dummy.next = head
        x = dummy

        while dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return x.next


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    head = solution.removeElements(node1, 1)
    solution.print(head)