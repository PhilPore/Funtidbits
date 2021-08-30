# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # Create a cycle and use the k rotations and length of the list to 
        # figure out how many of the right nodes you'll be moving to the
        # left. When you figure that out, move through the list till
        # you get to the point x where x's next element is the start of
        # the rotated list.
        # Set the head to x's next element and then set x's next element to         #None. This will break the cycle.
        
        if head == None or head.next == None:
            return head
        len_lst = 1
        t_head = head
        while t_head.next:
            len_lst+=1
            t_head = t_head.next
        true_rot = len_lst-(k%len_lst)
        t_head.next = head
        t_head = t_head.next
        for i in range(true_rot-1):
            #print(t_head.val)
            t_head = t_head.next
        head = t_head.next
        t_head.next = None
        #print(head.next.val)
        return head
