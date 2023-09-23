# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.LEFT = False
        self.RIGHT = True
        def findLeftBottom(node):
            if not node:
                return None
            cur = node
            while cur.left:
                cur = cur.left
            return cur
        def findRightBottom(node):
            if not node:
                return None
            cur = node
            while cur.right:
                cur = cur.right
            return cur
        if not root:
            return None
        elif root.val == key:
            if root.left and root.right:
                bottom = findRightBottom(root.left)
                bottom.right = root.right
                return root.left
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None
        head = root
        cur = head
        last_dir = False
        prev = None
        while cur and cur.val != key:
            prev = cur
            if cur.val > key:
                cur = cur.left
                last_dir = self.LEFT
            else:
                cur = cur.right
                last_dir = self.RIGHT
        if not cur:
            return head
        if last_dir == self.LEFT:
            tmp = cur.left
            if cur.right:
                prev.left = cur.right
                bottom = findLeftBottom(prev.left)
                bottom.left = tmp
            else:
                prev.left = tmp
        else:
            tmp = cur.right
            if cur.left:
                prev.right = cur.left
                bottom = findRightBottom(prev.right)
                bottom.right = tmp
            else:
                prev.right = tmp
        return head
        
        
