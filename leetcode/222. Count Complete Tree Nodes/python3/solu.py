# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getTreeHeight(root: TreeNode) -> int:
    height = 0
    curNode = root
    while (None != curNode):
        curNode = curNode.left
        height += 1
    return height

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        height = getTreeHeight(root)
        print('height: ', height)
        upperPartCnt = (2 ** (height - 1) ) - 1
        print('upperPartCnt: ', upperPartCnt)
        
