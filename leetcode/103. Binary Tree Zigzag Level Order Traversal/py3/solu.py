# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if None == root:
#             return []
#         que = []
#         que.append(root)
#         res = []
#         is_left_to_right = True
#         while len(que):
#             lvlnodeval = deque()
#             lvlcnter = 0
#             leng = len(que)
#             # print('lvlcnter: ', lvlcnter, ', leng: ', leng)
#             while (lvlcnter < leng):
#                 lvlcnter += 1
#                 node = que.pop(0)
#                 if not is_left_to_right:
#                     lvlnodeval.appendleft(node.val)
#                 else:
#                     lvlnodeval.append(node.val)
                    
#                 children = []
#                 children.append(node.left)
#                 children.append(node.right)
#                 for c in children:
#                     if c:
#                         que.append(c)
                
#                 print('lvlnodeval: ', lvlnodeval)
#             res.append(lvlnodeval)
#             is_left_to_right = not is_left_to_right
#             print('is_left_to_right: ', is_left_to_right)
                
#         print('res: ', res, '\n\n')
#         return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        lvl_list = deque()
        if None is root:
            return []
        # start with lvl 0 with a delimiter?
        node_queue = deque([root, None])
        is_order_left = True
        
        while len(node_queue) > 0:
            cur_node = node_queue.popleft()
            if cur_node:
                # lvl_list.append(cur_node.val)
                if is_order_left:
                    lvl_list.append(cur_node.val)
                else:
                    lvl_list.appendleft(cur_node.val)

                if cur_node.left:
                    node_queue.append(cur_node.left)
                if cur_node.right:
                    node_queue.append(cur_node.right)
                    
            else:
                # finished 1 lvl.
                ret.append(lvl_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)
                
                # prepare for the next level.   
                lvl_list = deque()
                is_order_left = not is_order_left
                
        return ret