
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
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        if (nullptr == t1 && nullptr == t2) {
            return true;
        }
        if (nullptr == t1 || nullptr == t2) {
            return false;
        }
        
        return (t1->val == t2->val) 
            && isMirror(t1->right, t2->left)
            && isMirror(t1->left, t2->right);
        
    }
        
    bool isSymmetric(TreeNode* root) {
        return isMirror(root, root);
        
    }
};
