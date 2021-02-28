# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while (None != root or stack):
            while(None != root):
                stack.append(root)
                print('stack: ', root.val)
                root = root.left

            root = stack.pop()
            k -= 1
            if (0 == k):
                break
            root = root.right

        return root.val



        