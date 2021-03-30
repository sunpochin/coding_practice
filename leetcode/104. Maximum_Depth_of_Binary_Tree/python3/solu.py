# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, node: TreeNode, curDepth):
        if (not node):
            return curDepth
        curDepth += 1
        return max(self.recur(node.left, curDepth), 
                    self.recur(node.right, curDepth) )

    
    def maxDepth(self, root: TreeNode) -> int:
        return self.recur(root, 0)
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        que = []
        res = []
        que.append(root)
        BFlen = 1
        
        while(len(que)):
            node = que.pop(0)
            res.append(node)
            if (len(res) < BFlen):
                # continue
                print('< que: ', que)
                
                if (node.left):
                    que.append(node.left)
                if (node.right):
                    que.append(node.right)
            else:
                res.append(que)
                print('this lvl done, que: ', que)
                
            
            
        return res
    
    
    

