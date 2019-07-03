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
    bool hasCycle(ListNode *head) {
        set<ListNode *> nodetraveled;
        
        
        if (nullptr == head) {
            return false;
        }
        while(head != nullptr) {
            if (nodetraveled.find(head) != nodetraveled.end() ) {
                return true;
            } else {
                nodetraveled.insert(head);
            }
            head = head->next;
        }
        
        return false;
        
    }
};

