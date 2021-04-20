# # BFS solution.
# #
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         que = []
#         res = []
#         if None == root:
#             return res
#         que.append(root)
#         while(len(que)):
#             leng = len(que)
#             cnt = 0
#             curlvlval = []
#             while(cnt < leng):
#                 node = que.pop(0)
#                 curlvlval.append(node.val)
#                 cnt += 1
#                 if (node.left):
#                     que.append(node.left)
#                 if (node.right):
#                     que.append(node.right)
#             res.append(curlvlval)
#             # print('res: ', res)
#             # print('que: ', que)
            
#         return res
                
                

# DFS solution.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFSlvlhelper(self, res: List[List[int]], node: TreeNode, height: int):
        if (None == node):
            return
        lvlval = []
        if (height >= len(res) ):
            print('Change lvl, height: ', height, ', len(res): ', len(res))
            res.append(lvlval)
        res[height].append(node.val)
        print('height: ', height, ', res[height]: ', res[height] )
        self.DFSvlvlhelper(res, node.left, height + 1)
        self.DFSlvlhelper(res, node.right, height + 1)       
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.DFSlvlhelper(res, root, 0)
        return res

