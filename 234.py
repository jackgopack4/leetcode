# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLinkedList(self,head):
        # returns pointer to reversed linked list with last node having "None" as next
        prev = None
        cur = head
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    def returnEvenLengthList(self,head,length):
        i = 0
        mid = length / 2
        cur = head
        prev = head
        while i<mid:
            prev = cur
            cur = cur.next
            i+=1
        prev.next = cur.next
        return head
    def getLength(self,head):
        cur = head
        i = 0
        while cur != None:
            cur = cur.next
            i+=1
        return i
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = self.getLength(head)
        mid = length / 2
        if length == 1: return True
        
        if length % 2 != 0:
            head = self.returnEvenLengthList(head,length)
            length-=1
        i=0
        cur = head
        while i<mid:
            cur = cur.next
            i+=1
        rightHalf = self.reverseLinkedList(cur)
        leftHalf = head
        
        while rightHalf != None:
            if leftHalf.val != rightHalf.val: return False
            leftHalf = leftHalf.next
            rightHalf = rightHalf.next
        return True
            
