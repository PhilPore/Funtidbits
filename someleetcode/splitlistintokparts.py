# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        
        Big thing to notice is that we can calculaste how many elements
        to put in the list via length/k. However, we need to get the               remainder. The amount of iterations equal to the remainder will need to be increased by 1. 
        
        FOr example, if we have 10 elements that we want to split into k groups. We'd get width 3, remainder 1. In that remainder 1 iteration (which will be the first), the width would increase to 4; leaving an equal number of elements that will fit the remaining groups (leaves 6 left, meaning 3 elements for the last 2 iterations), as the earlier parts of our return array needs to be greater than by 1 or equal to the later parts.
        """
        t_head = head
        ret_arr = []
        len_l = 0
        while t_head:
            len_l+=1
            t_head = t_head.next
        #capac = 1
        width = len_l//k
        rem = len_l%k
        #trav_head = head
        cur_node = head
        for i in range(k):
            t_head = cur_node
            #print(width + (i < rem)-1)
            for j in range(width + (i < rem)-1): #because remember, start at 0
                if cur_node: cur_node = cur_node.next
            if cur_node:
                temp = cur_node.next
                cur_node.next = None
                cur_node = temp
            ret_arr.append(t_head)
        return ret_arr
