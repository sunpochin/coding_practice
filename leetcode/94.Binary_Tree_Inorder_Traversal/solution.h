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
    
    void helper(TreeNode* root, vector<int>& res) {
        if (nullptr != root) {


            if (nullptr != root->left) {
                helper(root->left, res);
            }
            
            res.push_back(root->val);
            
            if(nullptr != root->right) {
                helper(root->right, res);
            }

        
        }
    }
    
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        helper(root, res);
        return res;
        
    }
};