# 21. Merge two sorted lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = list1
        cur2 = list2
        list3 = None
        if cur1:
            if cur2:
                if cur1.val > cur2.val:
                    list3 = cur2
                    cur2 = cur2.next
                else: 
                    list3 = cur1
                    cur1 = cur1.next
            else:
                list3 = cur1
                cur1 = cur1.next
        else:
            if cur2:
                list3 = cur2
                cur2 = cur2.next
        cur3 = list3
        while cur1 or cur2:
            if cur1 and (not cur2):
                cur3.next = cur1
                cur1 = cur1.next
                cur3 = cur3.next
            elif (not cur1) and cur2:
                cur3.next = cur2
                cur2 = cur2.next
                cur3 = cur3.next
            else:
                if cur1.val > cur2.val:
                    cur3.next = cur2
                    cur2 = cur2.next
                    cur3 = cur3.next
                else:
                    cur3.next = cur1
                    cur1 = cur1.next
                    cur3 = cur3.next
        return list3
