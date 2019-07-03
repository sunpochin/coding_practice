
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode *> theSet;
        
        while (nullptr != headA) {
            theSet.insert(headA);
            headA = headA->next;
            
        }
        
        while (nullptr != headB) {
            if (theSet.find(headB) != theSet.end() ) {
                return headB;
            }
            headB = headB->next;
        }

        
        return nullptr;
        
    }
};

