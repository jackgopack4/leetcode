# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q = deque()
        q.append((root,targetSum-root.val))
        while q:
            cur, cur_sum = q.pop()
            if not cur.left and not cur.right and cur_sum == 0:
                return True
            if cur.right:
                q.append((cur.right,cur_sum-cur.right.val))
            if cur.left:
                q.append((cur.left,cur_sum-cur.left.val))
        return False
