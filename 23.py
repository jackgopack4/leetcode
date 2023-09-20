import heapq
# Definition for singly-linked list.
# LEETCODE HARD
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = []
        heapify(pointers)
        for i,l in enumerate(lists):
            if l:
                heappush(pointers,(l.val,i))
                lists[i] = lists[i].next
        if pointers:
            val, idx = heappop(pointers)
            if lists[idx]:
                heappush(pointers,(lists[idx].val,idx))
                lists[idx] = lists[idx].next
            new_list = ListNode(val)
            cur = new_list
        else:
            new_list = None
        while pointers:
            val, idx = heappop(pointers)
            if lists[idx]:
                heappush(pointers,(lists[idx].val,idx))
                lists[idx] = lists[idx].next
            cur.next = ListNode(val)
            cur = cur.next
        return new_list
