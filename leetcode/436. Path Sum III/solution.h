// A path can start at any node and go down. We have to consider the cumulative number due to all of them. The procedure would be:

// Fix a node as the path's starting point.
// Calculate the number of paths that can come out of this node.
// Do this for all the nodes.
// Sum up the total number of paths.


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
    int pathSum(TreeNode* root, int sum) {
        int res = 0;
        inorder(root, sum, res);
        return res;
    }
    
    void inorder(TreeNode* root, int sum, int& res) {
        if (!root) {
            return;
        }
        pathSum(root, 0, sum, res);
        
        inorder(root->left, sum, res);
        inorder(root->right, sum, res);
    }
    
    void pathSum(TreeNode *root, int curSum, int sum, int& res) {
        if (!root) {
            return;
        }
        curSum += root->val;
        if (curSum == sum) {
            res++;
        }
        pathSum(root->left, curSum, sum, res);
        pathSum(root->right, curSum, sum, res);
    }
};
