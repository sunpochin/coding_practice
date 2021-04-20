# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyhead = ListNode(0)
        p, q, curr = l1, l2, dummyhead
        carry = 0
        
        while (p != None or q != None):
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if (p != None):
                p = p.next
            if q != None:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummyhead.next
        
        
#         res = []
#         carry = 0
#         p1 = len(num1) - 1
#         p2 = len(num2) - 1
#         print('p1: ', p1, ', p2: ', p2)
#         while p1 >= 0 or p2 >= 0:
#             x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
#             print('ord(num1[p1]): ', ord(num1[p1]), ', ord(0): ', ord('0'), ', x1: ', x1)

#             x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
#             print('ord(num2[p2]): ', ord(num2[p2]), ', ord(0): ', ord('0'), ', x2: ', x2)
            
#             value = (x1 + x2 + carry) % 10
#             print('value: ', value, ', carry:', carry)
#             carry = (x1 + x2 + carry) // 10
#             print('carry: ', carry)
#             res.append(value)
#             p1 -= 1
#             p2 -= 1
        
#         if carry:
#             res.append(carry)
        
#         return ''.join(str(x) for x in res[::-1])
        
        