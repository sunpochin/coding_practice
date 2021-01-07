# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode(-1)
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
                print('l2: ', l2)
            else:
                tail.next = l1
                l1 = l1.next
                print('l1: ', l1)
            print('tail: ', tail)
            tail = tail.next
            print('tail: ', tail, '\n')
            
        
        