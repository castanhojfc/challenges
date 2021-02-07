class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()

    one = Node(1)
    two = Node(2)
    three = Node(3)

    one.next = two
    one.prev = None

    two.next = three
    two.prev = one

    three.next = None
    three.prev = two

    head = one
