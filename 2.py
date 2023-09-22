# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addTwoDigits(overflow_in:bool,n1:int,n2:int) ->(int,bool):
            tmp = n1 + n2
            if overflow_in:
                tmp += 1
            if tmp >= 10:
                return (tmp-10,True)
            else:
                return (tmp,False)
        ret_val, overflow = addTwoDigits(False,l1.val,l2.val)
        l1 = l1.next
        l2 = l2.next
        ret = ListNode(ret_val)
        cur = ret
        while l1 and l2:
            nex_val, overflow = addTwoDigits(overflow,l1.val,l2.val)
            cur.next = ListNode(nex_val)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            tmp = l1
        elif l2:
            tmp = l2
        else:
            tmp = None
        while tmp:
            nex_val, overflow = addTwoDigits(overflow,tmp.val,0)
            cur.next = ListNode(nex_val)
            cur = cur.next
            tmp = tmp.next
        if overflow:
            cur.next = ListNode(1)
            overflow = False
        return ret
