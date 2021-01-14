# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = None
        second = None
        length = 0
        first = head
        while(first != None):
            first = first.next
            length += 1
        print('length: ', length)
        
        first = dummy
        for ni in range(length - n):
            first = first.next
        print('first: ', first)
#        if (first.next != None):
        first.next = first.next.next
        
        return dummy.next
            
