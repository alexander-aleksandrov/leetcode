from linked_list import LinkedList 

def test_linked_list():
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    assert llist.head.data == 1
    assert llist.tail.data == 2

def test_reversed():
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.reverse_iterative()
    assert llist.head.data == 4
    assert llist.tail.data == 1

