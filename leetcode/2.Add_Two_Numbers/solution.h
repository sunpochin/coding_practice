/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0, sum = 0;
        ListNode pre_head(-1);
        ListNode* ptr = &pre_head;
        
//        ListNode* ptr = new ListNode(-1);
        ListNode* head = ptr;
        
        while( l1 or l2 or carry ) {
            if( l1 ) {
                sum += l1->val;
                l1 = l1->next;
            }
            if( l2 ) {
                sum += l2->val;
                l2 = l2->next;
            }

            if( carry ) {
                sum += carry;
                carry = 0;
            }

            carry = sum / 10;
            sum = sum % 10;
            ptr->next = new ListNode( sum );
            ptr = ptr->next;
            sum = 0;        
        }

		/*End the result Linked list with nullptr and return the node next to pre_head*/
        ptr->next = nullptr;
        head = pre_head.next;
        
        return head;
        
    }
};
