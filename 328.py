# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_cur = head
        even_head = head.next if head else None
        even_cur = even_head
        odd_prev = odd_cur
        while odd_cur and even_cur:
            tmp_odd = even_cur.next
            if tmp_odd:
                tmp_even = tmp_odd.next
            else:
                tmp_even = None
            odd_cur.next = tmp_odd
            even_cur.next = tmp_even
            odd_prev = odd_cur
            odd_cur = odd_cur.next
            even_cur = even_cur.next
        if odd_cur:
            odd_cur.next = even_head
        elif odd_prev:
            odd_prev.next = even_head
        return head
