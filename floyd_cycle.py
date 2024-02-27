class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
     
    def data(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def floyd_cycle(llist):
    slow = llist.head 
    fast = llist.head
    met = False
    while fast.next is not None :
        slow = slow.next 
        fast = fast.next.next
        if fast == slow: 
            met = True 
            break
    if not met: 
        return None
    else: 
        slow = llist.head 
        while slow != fast: 
            slow = slow.next 
            fast = fast.next
        return slow

def floyd_cycle_in_array(arr):
    slow = 0
    fast = 0
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            slow = 0
            break
    while slow!=fast: 
        slow = arr[slow]
        fast = arr[fast]
    return slow
        

def main():
    # Floyd's cycle detection unit test
    llist = LinkedList()
    llist.append(20)
    llist.append(4)
    llist.append(15)
    llist.append(10)
    llist.append(25)
    llist.append(10)
    llist.head.next.next.next.next.next.next = llist.head.next.next
    
    print(floyd_cycle(llist).data)
    
if __name__ == "__main__":
    main()