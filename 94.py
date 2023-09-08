// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        if root:
            stack.append(root)
        res = []
        while stack:
            cur = stack.pop()
            if cur.left and cur.right:
                stack.append(cur.right)
                stack.append(cur)
                stack.append(cur.left)
                cur.left = None
                cur.right = None
            elif cur.left:
                stack.append(cur)
                stack.append(cur.left)
                cur.left = None
            elif cur.right:
                stack.append(cur.right)
                stack.append(cur)
                cur.right = None
            else:
                res.append(cur.val)
        return res
                    