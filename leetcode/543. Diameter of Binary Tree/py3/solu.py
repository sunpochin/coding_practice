# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # DFS
        def dfs(node: TreeNode):
            if None == node:
                return 0
            # self.answer += 1
            leftlen = dfs(node.left) 
            rightlen = dfs(node.right) 
            self.diameter = max(self.diameter, leftlen + rightlen)
            ret = max(leftlen, rightlen) + 1
            print('self.diameter: ', self.diameter, ', ret: ', ret)
            # print('leftlen: ', leftlen, ', rightlen: ', rightlen, ', ret: ', ret)
            return ret
            
        leng = dfs(root)
        print('answ: ', leng, ', self.diameter: ', self.diameter)
        return self.diameter
        