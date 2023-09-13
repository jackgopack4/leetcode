# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        i = 1
        queue.append((root,i))
        curr_max = [i,root.val]
        running_total = 0
        
        while queue:
            cur, lvl = queue.popleft()
            if lvl > i:
                if running_total > curr_max[1]:
                    curr_max = [i,running_total]
                i = lvl
                running_total = 0
            running_total += cur.val
            if cur.left:
                queue.append((cur.left,lvl+1))  
            if cur.right:
                queue.append((cur.right,lvl+1)) 
        if running_total > curr_max[1]:
            curr_max = [i,running_total]
        return curr_max[0]
            
