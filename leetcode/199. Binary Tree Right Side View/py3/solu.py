# BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:



# # DFS
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         lvlreached = -1
#         ans = []
#         def traverse(self, node: TreeNode, lvl: int):
#             if None == node:
#                 return
#             # print('node: ', node.val)
#             # if not yet visited this level before, add right-most node value.
#             if (lvl > lvlreached):
#                 lvlreached = max(lvlreached, lvl)
#                 # print('Solution.lvlreached: ', Solution.lvlreached, ', Solution.ans: ', Solution.ans)
#                 ans.append(node.val)
#     #        lvl += 1
#             self.traverse(node.right, lvl + 1)
#             self.traverse(node.left, lvl + 1)
            
#         # if None == root:
#         #     return ans
#         self.traverse(root, 0)

#         return ans




