#Link: https://leetcode.com/problems/merge-intervals/ I submitted with my jank solution (commented out on the bottom). I found the better solution to look much nicer.
#There is also an N^2 solution that involves graphs but that seems like overkill and also takes more time. 
#It will be interesting to read it and try to figure out why someone made that solution.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        '''
        The better solution
        intervals.sort(key=lambda x: x[0])
        
        ans = []
        for each in intervals:
            if len(ans) == 0 or ans[-1][1] < each[0]:
                ans.append(each)
            else:    
                ans[-1][1] = max(ans[-1][1], each[1])
            
        return ans
        
        '''
        intervals.sort(key=lambda x:x[0])
        ret = []
        for ranges in intervals:
            #print(ranges)
            if len(ret) == 0 or ret[-1][1] < ranges[0]:
                ret.append(ranges)
            else:
                ret[-1][1] = max(ret[-1][1],ranges[1])
        return ret
        '''
        the overcomplicated crappy (my solution)
        if len(intervals) == 1:
            return intervals
        #sort by first of the interval
        intervals = sorted(intervals, key = lambda x: x[0])
        
        arr = []
        trev = 0
        while trev < len(intervals)-1:
            unchanged = True
            skip = 0
            temp = intervals[trev]
            if intervals[trev][1] >= intervals[trev+1][0]:
                unchanged = False
                #temp = None
                for i in range(trev+1,len(intervals)):
                    if intervals[i][0] <= temp[1]:
                        print(intervals[i])
                       
                        temp = [min(temp[0],intervals[i][0]),max(intervals[i][1],temp[1])]
                        skip+=1
                    else:
                        break
                    #print(temp)
                    
            arr.append(temp)
            trev+=1+skip
        #print(arr)
        #print(trev)
        #print("--")
        if trev < len(intervals) and intervals[trev][1] > arr[-1][1]:
            arr.append(intervals[trev])
        return arr
                
        '''   
