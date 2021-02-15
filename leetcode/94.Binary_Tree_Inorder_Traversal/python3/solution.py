# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        list = []
        stack = []
        while( root != None or stack):
            while(root != None):
                stack.append(root)
                print('stack: ', root.val)
                root = root.left
            
            root = stack.pop()
            list.append(root.val)
            print('list: ', root.val)
            root = root.right
        
        
        return list
        