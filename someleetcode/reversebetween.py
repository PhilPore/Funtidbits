def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
        #effectively reverse everything in left-right, 
        # but keep track of the node after that. When thats done. 
        # move the  curr naode up to left, keep track of the prev
        # make tail = curr, tail of reverse
        # con = prev
        # temp = cur.next -> cur.next = prev -> prev = cur -> cur = third
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # iwhere l = 2, cur becomes 2, and prev becomes 1. If we want to reverse from pos 2-4,
        # we'll have to do the above operations. Do it on your own to refresh your memory 
        # then we set con.next to the new prev, if con exists. If not, then head.next
        # after that, set tail.next to be cur. This is because cur will always 
        # reach the element after the range
        # Donezo
        if not head:
            return None
        cur = head
        prev = None
        while left > 1:
            prev = cur
            cur = cur.next
            left -=1
            right-=1
        tail = cur
        con = prev
        n = right
        while n > 0:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n-=1
        
        if con:
            con.next = prev
        else:
            head = prev
        #print(tail.val)
        #print(cur.val)
        tail.next = cur
        return head
        '''
        buffer = []
        trav = head
        for i in range(left-1):
            trav = trav.next
        temp_run = trav
        for i in range(left, right+1):
            buffer.append(temp_run.val)
            temp_run = temp_run.next
        print(buffer)
        s_idx = len(buffer)-1
        for i in range(left,right+1):
            trav.val = buffer[s_idx]
            s_idx-=1
            trav = trav.next
        return head
            
        '''