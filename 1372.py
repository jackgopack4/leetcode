# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.LEFT = 0
        self.RIGHT = 1
        self.longest = 0
        def dfs(root,last_dir,depth):
            if root:
                if depth > self.longest:
                    self.longest = depth
                if not root.left and not root.right:
                    return depth
                if depth == 0:
                    return max(dfs(root.left,self.LEFT,depth+1),dfs(root.right,self.RIGHT,depth+1))
                else:
                    if last_dir == self.LEFT:
                        return max(dfs(root.right,self.RIGHT,depth+1),dfs(root.left,self.LEFT,1))
                    else:
                        return max(dfs(root.right,self.RIGHT,1),dfs(root.left,self.LEFT,depth+1))
            else:
                return depth-1
        return dfs(root,0,0)
