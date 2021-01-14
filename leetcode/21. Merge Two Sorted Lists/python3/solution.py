# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(-1)
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                print('l2: ', l2)
                l2 = l2.next
            else:
                tail.next = l1
                print('l1: ', l1)
                l1 = l1.next
            print('head: ', head)
            tail = tail.next
            print('head: ', head)
            print('tail: ', tail, '\n')
            
        print('while end')
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return head.next
        