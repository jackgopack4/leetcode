# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        node_val_list = []
        cur = head
        while cur:
            node_val_list.append(cur.val)
            cur = cur.next
        if not node_val_list:
            return None
        def makeSubTree(parent:ListNode,left_list:List[int],right_list:List[int]):
            left_midpoint = len(left_list) // 2
            if len(left_list) == 1:
                parent.left = TreeNode(val=left_list[0])
            elif len(left_list) > 1:
                parent.left = TreeNode(val=left_list[left_midpoint])
                makeSubTree(parent.left,left_list[:left_midpoint],left_list[left_midpoint+1:])
            right_midpoint = len(right_list) // 2
            if len(right_list) == 1:
                parent.right = TreeNode(val=right_list[0])
            elif len(right_list) > 1:
                parent.right = TreeNode(val=right_list[right_midpoint])
                makeSubTree(parent.right,right_list[:right_midpoint],right_list[right_midpoint+1:])
        list_midpoint = len(node_val_list) // 2
        new_root = TreeNode(val=node_val_list[list_midpoint])
        makeSubTree(new_root,node_val_list[:list_midpoint],node_val_list[list_midpoint+1:])
        return new_root
