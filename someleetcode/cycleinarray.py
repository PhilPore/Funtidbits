class Solution(object):
    def _next(self, nums, indx, direct):
        if indx == -1: 
            #means we go back one, which brwings us back to the indx. 
            #means there is a sequence of len 1 which is no good.
            #aprimarily to handle fast.next = fast.next = -1
            return -1
        elif (nums[indx] > 0) != direct: 
            return -1
        next_idx = (indx+nums[indx])%len(nums)
        if next_idx < 0:
            next_idx+=len(nums)
        return -1 if next_idx == indx else next_idx

        
        
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        my assumption was that we'd have to start at 0 and thats that. 
        I didn't realize we could go indx+1 for checking for cycles.
        I believe I tried something similar but with no luck.
        '''
        for i in range(len(nums)):
            #print(self.__visited(nums[i]))
            if not nums[i]:
                continue
            direc = nums[i] > 0

            slow = i
            fast = i
            while not(not nums[slow] or not nums[fast]):
                slow = self._next(nums,slow,direc)
                fast = self._next(nums,self._next(nums,fast,direc), direc)
                if slow == -1 or fast == -1:
                    break
                elif slow == fast:
                    return True
            slow = i
            while self._next(nums,slow,direc) != -1:
                nums[slow],slow = 0, self._next(nums,slow,direc)
        return False
    
    
    """
    Solution involving sets
    def circularArrayLoop(self, nums):
        
        
                
        visited = set()
        for i in range(len(nums)):
            if i in visited:
                continue
            local_s = set()
            t = i
            #print("ooo")
            while True:
                #print(t)
                if t in local_s:
                    return True
                visited.add(t)
                local_s.add(t)
                prev = t
                t = (t+nums[t])%len(nums)
                #print(t)
                #print(nums[prev])
                #print(nums[t])
                #print("00")
                #print(prev == t)
                #print((nums[prev] > 0) != (nums[t] > 0))
                if prev == t or ((nums[prev] > 0) != (nums[t] > 0)):
                    break
        return False
    """      
        