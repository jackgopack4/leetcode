# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1leafs = []
        root2leafs = []
        def inOrderTraversalWithLeaf(node, array):
            if node is not None:
                inOrderTraversalWithLeaf(node.left,array)
                if node.left is None and node.right is None: # child
                    array.append(node.val)
                inOrderTraversalWithLeaf(node.right,array)
        inOrderTraversalWithLeaf(root1,root1leafs)
        inOrderTraversalWithLeaf(root2,root2leafs)
        return root1leafs == root2leafs
