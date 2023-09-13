# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.right_side = []
        def bfs(node):
            stack = deque()
            i = 0
            if node:
                stack.append((node,i))
                while stack:
                    cur, lvl = stack.popleft()
                    if lvl == i:
                        i += 1
                        self.right_side.append(cur.val)
                    if cur.right:
                        stack.append((cur.right,i))
                    if cur.left:
                        stack.append((cur.left,i))
        bfs(root)
        return self.right_side
