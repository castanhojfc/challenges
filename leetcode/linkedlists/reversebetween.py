"""
Problem:
Reverse linked list within a range.

Solution:
Traverse the linked list.
Keep track of four things:

Considering that the range is given by m and n.

1) Previous node from m.
2) m.
3) n.
4) Next node of n.

Detach n by pointing the next node to None.
Reverse the nodes using the standard strategy and using m.
Set the previous node from m next node to the head of the reversed sub list.
Connect the rest of the list using the next node of n to the start node.
The start node should now be at the end.
If m is the headit self, no need to connect the first part to the previous node.

Runtimes:
Time: O(n)
Spcae: O(1)

https://leetcode.com/problems/reverse-linked-list-ii/
"""

from commons import printLinkedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverse(self, head):
        prev = None
        curr = head

        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        start_reverse_node = None
        end_reserve_node = None
        previous_node = None
        next_node = None

        i = 1
        curr = head

        while(curr and i <= n):
            if(i < m):
                previous_node = curr

            if(i == m):
                start_reverse_node = curr

            if(i == n):
                end_reserve_node = curr
                next_node = curr.next

            curr = curr.next
            i += 1

        end_reserve_node.next = None

        end_reserve_node = self.reverse(start_reverse_node)

        if(previous_node):
            previous_node.next = end_reserve_node
        else:
            head = end_reserve_node

        start_reverse_node.next = next_node

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

    head = solution.reverseBetween(node1, 2, 4)
    printLinkedList(head)