// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        queue.append((root,0))
        level = 0
        while queue:
            cur, level = queue.popleft()
            if cur:
                if len(res) > level:
                    res[level].append(cur.val)
                else:
                    res.append([cur.val])

                if cur.left:
                    queue.append((cur.left,level+1))
                if cur.right:
                    queue.append((cur.right, level+1))
        return res
                
                
            
            