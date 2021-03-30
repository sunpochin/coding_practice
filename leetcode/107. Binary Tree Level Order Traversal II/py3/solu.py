# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if (None == root):
            return []
        queue = []
        queue.append(root)
        
        while(len(queue) > 0):
            cnter = 0
            leng = len(queue)
            lvlnodeval = []
            while (cnter < leng):
                cnter += 1
                node = queue.pop(0)
                print('node: ', node.val)
                lvlnodeval.append(node.val)
                if (node.left):
                    queue.append(node.left)
#                     lvlnodeval.append()
                if (node.right):
                    queue.append(node.right)
            # end of while loop, push lvlnodeval into res
            res.append(lvlnodeval)
        
        res.reverse()
        
        return res
        