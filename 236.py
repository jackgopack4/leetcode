# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,p,q):
            root.parent = None
            stack = [root]
            self.pq = []
            while stack and len(self.pq)<2:
                cur = stack.pop()
                if cur == p or cur == q:
                    self.pq.append(cur)
                if cur.left:
                    cur.left.parent = cur
                    stack.append(cur.left)
                if cur.right:
                    cur.right.parent = cur
                    stack.append(cur.right)
        def findParent(child,parent):
            cur = child.parent
            while cur:
                if cur == parent:
                    return True
                cur = cur.parent
            return False
        dfs(root,p,q)
        if findParent(p,q):
            return q
        elif findParent(q,p):
            return p
        else:
            seen = set()
            cur = self.pq.pop().parent
            while cur:
                seen.add(cur)
                cur = cur.parent
            cur = self.pq.pop().parent
            while cur:
                if cur in seen:
                    return cur
                cur = cur.parent
            return None
