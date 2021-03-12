# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # head: 1 -> 2 -> 3 -> 4 -> 5 -> null
        # to 
        # head: 5 -> 4 -> 3 -> 2 -> 1 -> null
        
        # Example,
        # 1 -> 2   , to 
        # 2 -> 1 -> null
        
        # Algorithm:
        # 1. Remember "next node of cur node", avoiding cut off linked list. 
        # prev = curNode.next
        # 2. Change the direction of cur node, 
        # curNode.next to prev
        # 3. Remember "cur node" into "prev"
        #
        # 4. All previous 3 moves done, we reverse the links of 
        # "curNode to its next" and "the node linking to curNode".
        # Move curnode to next one in the linked list.


        # To remember the previous node of curNode.
        # also which node the REVERSED curNode.next should set to.
        prev = None
        # # to remember which node the next curNode.next should set to.
        # next = null
        curNode = head

        while(curNode):         # 1
            # perform some action.
            # which node be the REVERSED list head 
            next = curNode.next # 2
            curNode.next = prev
            prev = curNode
            curNode = next      #

        return prev

