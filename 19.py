# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = deque() # keep n+1 nodes here so we can replace pointers
        cur = head
        while cur:
            q.append(cur)
            if len(q) > n+1:
                q.popleft()
            cur = cur.next
        if len(q) == 1:
            return None
        elif n == 1:
            q[0].next = None
        elif len(q) == n:
            return q[1]
        else:
            q[0].next = q[2]
        return head
