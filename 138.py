"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_dict = {}
        cur = head
        while cur:
            node_dict[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                node_dict[cur].random = node_dict[cur.random]
            if cur.next:
                node_dict[cur].next = node_dict[cur.next]
            cur = cur.next
        return node_dict[head]
