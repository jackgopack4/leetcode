# Leetcode medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def overflowAdder(self, cur1: int, num2: int,overflow:int = 0) -> int:
        tmp = cur1.val+num2+overflow
        if tmp>9:
            cur1.val = tmp-10
            return 1
        else:
            cur1.val = tmp
            return 0
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        overflow = 0
        while cur1 != None or cur2 != None:
            print('overflow =  %d' % overflow)
            if cur1 != None and cur2 != None:
                prev1 = cur1
                prev2 = cur2
                overflow = self.overflowAdder(cur1,cur2.val,overflow)
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1 != None:
                prev1 = cur1
                overflow = self.overflowAdder(cur1,0,overflow)
                cur1 = cur1.next
            else: # cur1 None but cur2 valid
                prev2 = cur2
                prev1.next = ListNode()
                cur1 = prev1.next
                prev1 = cur1
                overflow = self.overflowAdder(cur1,cur2.val,overflow)
                cur1 = cur1.next
                cur2 = cur2.next
        if overflow == 1:
            prev1.next = ListNode(val=1)
        return l1
