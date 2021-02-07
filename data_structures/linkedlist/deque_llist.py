import collections
import llist
from llist import sllist, sllistnode

# can be used for linked lists
# only use to insert elements at the start and end
# in the middle it is time consuming
# there is no implementation in python

linked_list = collections.deque()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print(linked_list)

linked_list.insert(1, 6)

print(linked_list)

linked_list.pop()

print(linked_list)

linked_list.remove(6)

print(linked_list)

lst = sllist(['first', 'second', 'third'])
lst.append('fourth')
node = lst.nodeat(2)
lst.insertafter('fifth', node)
lst.pop()
node = lst.nodeat(1)
lst.remove(node)

print(lst)
print(lst.first)
print(lst.last)
print(lst.size)