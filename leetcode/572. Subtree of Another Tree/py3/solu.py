# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(s, t) -> bool:
            if None == s and None == t:
                return True
            if None == s or None == t:
                return False
            return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)

        def traverse(node: TreeNode, t):
            return None != node and (isSame(node, t) or traverse(node.left, t) or traverse(node.right, t) )
        
        ret = traverse(s, t)
        return ret

        