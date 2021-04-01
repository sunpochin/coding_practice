# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Algorithm:
# 1. pass height into recur, height + 1.
# 2. if None == node: return height
# 3. update minimum height.


class Solution:
    def recur(self, node: TreeNode, height: int):
        if None == node:
            return height
        recur(node.left)
        recur(node.right)

    def minDepth(self, root: TreeNode) -> int:
        self.recur(root, 0)
        
        