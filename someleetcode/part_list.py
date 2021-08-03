# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return None
        less_head = ListNode(0)
        great_head = ListNode(0)
        less_tail = less_head
        great_tail = great_head
        h = head
        while h != None:
            if h.val < x:
                less_tail.next = h
                less_tail = less_tail.next 
                
                
            else:
                great_tail.next = h
                great_tail = great_tail.next
            h = h.next
        great_tail.next = None
        less_tail.next = great_head.next
        return less_head.next
      
"""
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return None
        less_head = None
        great_head = None
        less_tail = None
        great_tail = None
        h = head
        while h != None:
            if h.val < x:
                if less_head == None:
                    less_head = ListNode(h.val)
                    less_tail = less_head
                else:
                    less_tail.next = ListNode(h.val)
                    less_tail = less_tail.next
            if h.val >= x:
                if great_head == None:
                    great_head = ListNode(h.val)
                    great_tail = great_head
                else:
                    great_tail.next = ListNode(h.val)
                    great_tail = great_tail.next
            h = h.next
        if less_head:
            less_tail.next = great_head
            return less_head
        else:
            return great_head
        
        




"""
