# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        que = []
        res = []
        if None == root:
            return res
        que.append(root)
        while(len(que)):
            leng = len(que)
            cnt = 0
            curlvlval = []
            while(cnt < leng):
                node = que.pop(0)
                curlvlval.append(node.val)
                cnt += 1
                if (node.left):
                    que.append(node.left)
                if (node.right):
                    que.append(node.right)
            res.append(curlvlval)
            # print('res: ', res)
            # print('que: ', que)
            
        return res
                
                


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def traverse(self, node):
#         print('self.val: ', node.val)
#         if (None != node.left):
#             self.traverse(node.left)
#         if (None != node.right):
#             self.traverse(node.right)
        
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         self.traverse(root)




