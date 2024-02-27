from floyd_cycle import floyd_cycle, floyd_cycle_in_array, LinkedList, Node


def test_floyd_cycle():
    llist = LinkedList()
    llist.append(20)
    llist.append(4)
    llist.append(15)
    llist.append(10)
    llist.append(25)
    llist.append(10)
    llist.head.next.next.next.next.next.next = llist.head.next.next
    assert floyd_cycle(llist).data == 15

def test_floyd_cycle_in_array():
    arr = [4, 3, 7, 8, 6, 9, 2, 1, 5, 2]
    assert floyd_cycle_in_array(arr) == 2

