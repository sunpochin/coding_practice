
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    // int sum = 0;
    
    int recur(TreeNode* node) {
        int sum = 0;
        
        if (nullptr == node) {
            return 0;
        }
        int left = 0;
        int right = 0;
        if (nullptr != node->left) {
            if (nullptr == node->left->left && nullptr == node->left->right) {
                // base case.
                sum = sum + node->left->val;
            } else {
                // recursive case.
                sum = sum + recur(node->left);
            }
        }
        
        if (nullptr != node->right) {
            // recursive case.
            sum = sum + recur(node->right);
        }
        return sum;
    }
        
        
    int sumOfLeftLeaves(TreeNode* root) {
        return recur(root);
        
    }
    
    
};
