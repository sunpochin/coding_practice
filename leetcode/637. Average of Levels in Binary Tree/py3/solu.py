# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ret = []
        lvl_list = deque()
        if None is root:
            return []
        node_deque = deque([root, None])
        is_order_left = True
        lvl_sum = 0
        lvl_cnt = 0
        while len(node_deque) > 0:
            cur_node = node_deque.popleft()
            if cur_node:
                lvl_sum += cur_node.val
                # print('cur_node.val: ', cur_node.val, ', lvl_sum: ', lvl_sum)
                lvl_cnt += 1
                # if is_order_left:
                #     lvl_list.append(cur_node.val)
                # else:
                #     lvl_list.appendleft(cur_node.val)
                                    
                if cur_node.left:
                    node_deque.append(cur_node.left)
                if cur_node.right:
                    node_deque.append(cur_node.right)
            else:
                # print('lvl_sum: ', lvl_sum)
                lvl_ave = 0
                if lvl_cnt > 0:
                    lvl_ave = lvl_sum / lvl_cnt
                ret.append(lvl_ave)
                
                if len(node_deque) > 0:
                    node_deque.append(None)
                
                # prepare for the next level.   
                lvl_list = deque()
                lvl_sum = 0
                lvl_cnt = 0
                
                # is_order_left = not is_order_left
        return ret

    

