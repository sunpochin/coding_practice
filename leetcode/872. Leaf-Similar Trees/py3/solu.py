# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def getleaves(node: TreeNode, ret):
            if None == node.left and None == node.right:
                ret.append(node.val)
            if node.left:
                getleaves(node.left, ret)
            if node.right:
                getleaves(node.right, ret)

        ret1 = []
        getleaves(root1, ret1)
        ret2 = []
        getleaves(root2, ret2)
        if ret1 == ret2:
            return True
        else:
            return False