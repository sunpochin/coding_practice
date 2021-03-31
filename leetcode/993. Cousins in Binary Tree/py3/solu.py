# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Same depth. Different parent. Same Grand parent.
# 1. constraints?
# 2. test cases?
# 3. Should I use BFS or DFS search?

# class Solution:
#     # def recur(self, root: TreeNode, x: int, y: int):
#     def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
#         iscousins = False
        
#         if None == root:
#             return False
#         # BFS
#         queue = []
#         # None as delimiter
#         queue.append(root)
#         queue.append(None)
#         nodedepth = [None, None]
#         parent = [None, None]
#         depth = 0
#         while len(queue) > 0:
#             # print('len: ', len(queue))
#             lvlnodes = []
#             cur_node = queue.pop(0)
#             if cur_node:
#                 print('cur_node val: ', cur_node.val)
#                 children = [cur_node.left, cur_node.right]
#                 for c in children:
#                     if c:
#                         queue.append(c)
#                         if c.val == x:
#                             parent[0] = cur_node.val
#                             nodedepth[0] = depth + 1
#                         if c.val == y:
#                             parent[1] = cur_node.val
#                             nodedepth[1] = depth + 1
#                 # if cur_node.left:
#                 #     queue.append(cur_node.left)
#                 # if cur_node.right:
#                 #     queue.append(cur_node.right)
#             else:
#                 if len(queue) > 0:
#                     # push None as delimiter of depth.
#                     queue.append(None)
#                     depth += 1
#         print('parent: ', parent, ', nodedepth: ', nodedepth)
#         if (nodedepth[0] == nodedepth[1] and parent[0] != parent[1]):
#             iscousins = True
#         return iscousins

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, parent, depth, target):
            if node:
                if target == node.val:
                    return depth, parent
                tmp = dfs(node.left, node, depth + 1, target) or dfs(node.right, node, depth + 1, target) 
                return tmp
        dx, px, dy, py = dfs(root, None, 0, x) + dfs(root, None, 0, y)
        return dx == dy and px != py
    