/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    // 1 -> 2 -> 3 -> 4 -> 5 -> null ptr
    // ==>
    // 5 -> 4 -> 3 -> 2 -> 1 -> null ptr
    // 

    let curNode = head
    while(curNode) {
        // perform some operation.
        curNode = curNode.next
    }
    
};

