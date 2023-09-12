# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self,root,highest=-10000):
        if root:
            return self.goodNodes(root.left, max(highest,root.val)) + self.goodNodes(root.right,max(highest,root.val))+ (root.val >= highest)
        else:
            return 0
