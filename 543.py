# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def maxPath(root):
            if not root:
                return 0
            left_path = maxPath(root.left)
            right_path = maxPath(root.right)
            self.diameter = max(self.diameter,left_path+right_path)

            return max(left_path,right_path) + 1

        maxPath(root)
        return self.diameter
