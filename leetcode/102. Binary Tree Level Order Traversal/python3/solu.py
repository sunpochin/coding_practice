# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, node):
        print('self.val: ', node.val)
        if (None != node.left):
            self.traverse(node.left)
        if (None != node.right):
            self.traverse(node.right)
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.traverse(root)
        
        