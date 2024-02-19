# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1,  l2):
        extent = 0
        head = ListNode()
        current = head
        while l1 or l2 or extent != 0:
            if l1:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            sum = x + y + extent
            extent = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
        res = head.next 
        head = None
        return res
    
           

def main():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next

if __name__ == "__main__":
    main()

