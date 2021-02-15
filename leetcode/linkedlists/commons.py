class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printLinkedList(node) -> None:
    """
    Prints a linked list.
    """
    temp = node

    while (temp):
        print(temp.val, end="->")
        temp = temp.next

    print()