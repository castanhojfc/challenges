class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print(self) -> None:
        temp = self.head

        while (temp):
            print(temp.item, end="->")
            temp = temp.next

        print()

    def insertBegining(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, data, node):
        if not node:
            return

        new_node = Node(data)

        new_node.next = node.next
        node.next = new_node

    def insertEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def delete(self, position):
        if not self.head:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

        for i in range(position - 1):
            temp_node = temp_node.next

            if temp_node is None:
                break

        # not present
        if temp_node is None:
            return

        if temp_node.next is None:
            return

        next = temp_node.next.next
        temp_node.next = next


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    linked_list.head.next = second
    second.next = third

    linked_list.print()
    linked_list.insertBegining(1)
    linked_list.print()
    linked_list.insertAfter(6, linked_list.head)
    linked_list.print()
    linked_list.delete(4)
    linked_list.print()
    linked_list.delete(1)
    linked_list.print()

    # Circular linked list
    circular_linked_list = LinkedList()

    one = Node(1)
    two = Node(2)
    three = Node(3)

    one.next = two
    two.next = three
    three.next = one

    head = one
