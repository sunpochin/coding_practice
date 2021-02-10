# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        rootval = root.val
        pval = p.val
        qval = q.val
        print('rootval: ', rootval, ', pval: ', pval, ', qval: ', qval)
        if pval < rootval and qval < rootval:
            print('both lower')
            return self.lowestCommonAncestor(root.left, p, q)
        elif pval > rootval and qval > rootval:
            print('both higher')
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # found
            print('FOUND!')
            return root
        
        