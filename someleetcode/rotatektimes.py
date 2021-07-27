def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #cyclic 
        n = len(nums)
        k%=n
        count = 0
        start = 0
        while count < n:
            curr, prev = start, nums[start]
            while True:
                
                nex = (curr+k)%n
                temp = nums[nex]
                nums[nex] = prev
                prev = temp
                curr = nex
                count+=1
                if start == curr:
                    break
            start+=1
        
        
        '''
        normal with n space used
        arr = []
        shift = len(nums)-k
        for i in range(len(nums)):
            arr.append(nums[(shift+i)%len(nums)])
        
        for i in range(len(nums)):
            nums[i] = arr[i]
        '''
        
                     
        
        