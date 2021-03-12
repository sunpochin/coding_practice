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
    // algorithm:
    // 1. Save the ptr to next node continue.
    // 2. Perform some operation to current Node.
    

    let curNode = head
    let preNode = null
    while(curNode) {
        // perform some operation.
        // curNode = curNode.next

        // change link direction.
        nextNode = curNode.next
        curNode.next = preNode

        preNode = curNode
        curNode = nextNode
    }
    return preNode
    
};

