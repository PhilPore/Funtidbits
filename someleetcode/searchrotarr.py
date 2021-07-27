def search_rotation(arr, target): 
    nums = arr
    '''returns index of the target, assuming it can be found '''
    #note! has to be done in less than n time
    #idear: technically everything is sorted, just rotated
    #check middle index to see if the values are greater on both sides. 
    # If not, then adjust until you find the proper position. Then  treat it like a normal binary search.
    # treat like circular array. 
    # Note: seeking smaller value: when arr[i-1] > arr[i], we know its not found on this side
    # larger: when arr[i+1] < arr[i], we have a problemo
    #better solution that I found:
    low = 0
    high = len(nums)-1 #see, this would have been smart to do in my solution and probably would have been
    #incredibly effective as it grabs a valid index.
    while(low<=high):
        mid= (low+high)//2 #get the mid index between the upper bound index and lowerbound
        if nums[mid] == target: #did we jackpot?
            return mid
        elif nums[mid] <= nums[high]: #check to see if our value is less than upperbound, 
            #meaning its somewhat sorted
            if nums[mid] < target <=nums[high]: #is mid less  than target and is target <= high val
                low = mid+1 #increment low because we want a higher value for mid
            else:
                high = mid-1 # decrement high so we get a lower value for mid
        elif nums[low]<=nums[mid]: #we are in a rotated area where our mid value is greater than our low index val
            #so naturally, we want to get closer to our lowest point instead
            if nums[low]<=target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
    #base case
    return -1          


    '''
    Solution I made for leetcode problem:
    Works but its not as efficient as I am going to be searching a smidge less than N if the target doesnt exist
    The logic isa the same from the points above. Find a point where it seems nonrotated, and search ala 
    binary from there
    mid = len(nums)//2
        prev = mid if len(nums)%2 == 1 else mid-1
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            return 0
        
        while True:
            print((mid+1)%len(nums))
            if(nums[mid%len(nums)] < nums[(mid+1)%len(nums)]):
                break
            #prev+=1
            mid+=1
        print(mid%len(nums))
        #mid+=1
        #now we do the bin search
        for i in range(len(nums)//2*2):
            if nums[mid%len(nums)] == target:
                return mid%len(nums)
            if nums[mid%len(nums)] < target:
                mid+=1
            else:
                mid-=1
        if nums[mid%len(nums)] == target:
            return mid%len(nums)
        return -1

    '''
    '''
    This is too much
    if arr[0] == target: 
        return 0
    if arr[-1] == target:
        return len(arr)-1
    less_than = True
    mid_point = len(arr)//2
    prev = mid_point-1
    ahead = mid_point+1
    if arr[prev%len(arr)] > arr[mid_point] and arr[mid_point] < arr[ahead%len(arr)]:
        prev = mid_point
        mid_point+=1
        ahead+=1
    new_pointer = mid_point
    
    less_than = False if target > arr[mid_point] else True
    index = 0
    while index < mid_point+1:
        if arr[new_pointer%len(arr)] == target:
            return new_pointer%len(arr)
        if less_than:
            ahead = new_pointer-1
            #if arr[ahead%len(arr)] > arr[new_pointer]: original idea here but ah whateves. might come in handy
            #    return None
            new_pointer-=1
            ahead-=1

        else:
            new_pointer+=1
            #do the if statement if this dont work
        index+=1
    
    return None

    return [prev,mid_point,ahead, [arr[prev], arr[mid_point], arr[ahead]]]'''
def search(nums,target):
    l, r = 0, len(nums) - 1
        
    while l <= r:
        mid = (l+r) // 2
            
        if nums[mid] == target:
            return mid
            
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        
    return l