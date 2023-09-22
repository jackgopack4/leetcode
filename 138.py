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
        new_node_list = []
        cur = head
        count = 0
        while cur:
            node_dict[cur] = count
            new_node_list.append(Node(cur.val))
            cur = cur.next
            count += 1
        # length of list now in count
        for i in range(len(new_node_list)-1):
            new_node_list[i].next = new_node_list[i+1]
        cur = head
        count = 0
        idx = -1
        while cur:
            if cur.random:
                idx = node_dict[cur.random]
            else:
                idx = -1
            if idx >= 0:
                new_node_list[count].random = new_node_list[idx]
            cur = cur.next
            count += 1
        return new_node_list[0]
