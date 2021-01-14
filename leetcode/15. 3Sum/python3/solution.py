# Definition for singly-linked list.
#import ListNode

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, None)
        print('dummy: ', dummy.next)
        dummy.next = head
        second = ListNode(0, None)
        length = 0
        first = ListNode(0, None)
        print('type: ', type(head))
        print('type: ', type(first))
        while(first != None):
            # first.val
            first = first.next
            length += 1
        print('length: ', length)
        
        first = dummy
        for ni in range(length - n):
            first = first.next
        print('first: ', first)
        print('first.next: ', first.next)
#        if (first.next != None):
#        first.next = ListNode(first.next, first.next.next)
        
        return dummy.next
            
