"""
Problem:
Find if the linked list has a cycle.

Solution:
Maintain two pointers that start at the head.
While there are two next nodes, perform a loop.
Compute the two next nodes per each iteration.
If they are the same a cycle was found.

Runtimes:
Time: O(n)
Space: O(1)

https://leetcode.com/problems/linked-list-cycle/
"""

from commons import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        i = j = head

        while j and j.next and j.next.next:
            i = i.next
            j = j.next.next

            if i == j:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node1
    node4.next = node5

    print(solution.hasCycle(node1))