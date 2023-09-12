# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.highest = -10001
        self.leaf_count = 0
        self.visited = {}
    def goodNodes(self, root: TreeNode) -> int:
        def preOrderTraversal(node):
            cur = node
            if cur:
                self.visited[cur]=self.highest
                if cur.val >= self.highest:
                    self.leaf_count += 1
                    self.highest = cur.val
                preOrderTraversal(cur.left)
                preOrderTraversal(cur.right)
                self.highest = self.visited.pop(cur)
        self.visited.clear()
        self.highest = root.val
        self.leaf_count = 0
        preOrderTraversal(root)
        return self.leaf_count
