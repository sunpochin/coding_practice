# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0
        que = [root]
        while que:
            curnode = que.pop(0)
            if curnode.left: que.append(curnode.left)
            if curnode.right: que.append(curnode.right)
            if curnode.val >= low and curnode.val <= high:
                sum += curnode.val
            
        return sum
        