def printLinkedList(node) -> None:
    """
    Prints a linked list.
    """
    temp = node

    while (temp):
        print(temp.val, end="->")
        temp = temp.next

    print()