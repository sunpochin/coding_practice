# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []

    def sumRootToLeaf(self, root: TreeNode) -> int:
        def traverse(node, valstr):
            # if None == node:
            #     print('null: ', valstr)
            #     return
            if None == node.left and None == node.right:
                tmpstr = valstr + str(node.val)
                self.path.append(tmpstr)
                return
            inputstr = valstr + str(node.val)
            if node.left:
                traverse(node.left, inputstr)
            if node.right:
                traverse(node.right, inputstr)
        
        traverse(root, "")
        # print('path: ', self.path)
        sum = 0
        for it in self.path:
            sum += int(it, 2)
        return sum