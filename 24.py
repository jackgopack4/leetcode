# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if cur and cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            head = tmp
        else:
            return head
        cur = head.next.next
        prev = head.next
        while cur and cur.next:
            prev.next = cur.next
            cur.next = prev.next.next
            prev.next.next = cur
            prev = cur
            cur = cur.next

        return head
