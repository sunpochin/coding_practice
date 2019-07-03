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
    int depth = 0;
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        return max(1 + maxDepth(root -> left), 1 + maxDepth(root -> right));
        
    }
};

