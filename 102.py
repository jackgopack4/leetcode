# https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if root:
            q.append((root,1))
        while q:
            cur, lvl = q.popleft()
            if lvl > len(res):
                res.append([cur.val])
            else:
                res[-1].append(cur.val)
            if cur.left:
                q.append((cur.left,lvl+1))
            if cur.right:
                q.append((cur.right,lvl+1))
        return res
